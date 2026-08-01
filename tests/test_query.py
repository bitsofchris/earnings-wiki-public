"""Tests for space/query.py — the shared retrieval layer behind the chat and CLI.

Runs against the real corpus shipped in space/ (no fixtures to drift):
    python3 -m unittest discover tests
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "space"))
import query as q


class Corpus(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c = q.load()

    def test_load_shape(self):
        self.assertGreater(len(self.c["fragments"]), 1000)
        self.assertGreater(len(self.c["clusters"]), 50)
        self.assertIn("semis", self.c["sectors"])
        self.assertIn("scarcity", self.c["questions"])
        self.assertEqual(self.c["quarters"], sorted(self.c["quarters"]))

    def test_every_fragment_has_sector(self):
        self.assertTrue(all(f.get("sector") for f in self.c["fragments"]))


class Select(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c = q.load()

    def test_symbol_filter(self):
        out = q.select(self.c, symbols=["nvda"], k=100)
        self.assertTrue(out)
        self.assertTrue(all(f["ticker"] == "NVDA" for f in out))

    def test_sector_filter(self):
        out = q.select(self.c, sector="semis", k=100)
        self.assertTrue(out)
        self.assertTrue(all(f["sector"] == "semis" for f in out))

    def test_date_range(self):
        out = q.select(self.c, since="2026-01-01", until="2026-03-31", k=200)
        self.assertTrue(out)
        self.assertTrue(all("2026-01-01" <= f["date"] <= "2026-03-31" for f in out))

    def test_question_filter(self):
        out = q.select(self.c, questions=["scarcity"], k=50)
        self.assertTrue(out)
        self.assertTrue(all(f["question"] == "scarcity" for f in out))

    def test_text_ranking_is_on_topic(self):
        out = q.select(self.c, text="capex data center capacity", k=10)
        self.assertEqual(len(out), 10)
        hits = sum(1 for f in out if "capex" in f["text"].lower() or "capacity" in f["text"].lower()
                   or "data center" in f["text"].lower())
        self.assertGreaterEqual(hits, 5)

    def test_no_text_returns_newest_first(self):
        out = q.select(self.c, symbols=["AAPL"], k=5)
        dates = [f["date"] for f in out]
        self.assertEqual(dates, sorted(dates, reverse=True))

    def test_k_cap_and_empty_scope(self):
        self.assertEqual(len(q.select(self.c, k=7)), 7)
        self.assertEqual(q.select(self.c, symbols=["ZZZZ"]), [])

    def test_scoped_text_backfills_to_k(self):
        # zero-BM25-overlap text must not starve a large scope — backfill newest-first
        out = q.select(self.c, sector="semis", questions=["scarcity"],
                       text="xylophone zebra unrelated", k=10)
        self.assertEqual(len(out), 10)
        self.assertTrue(all(f["sector"] == "semis" and f["question"] == "scarcity" for f in out))

    def test_composed_filters(self):
        out = q.select(self.c, sector="semis", since="2026-01-01", questions=["forward"], k=50)
        self.assertTrue(all(f["sector"] == "semis" and f["date"] >= "2026-01-01"
                            and f["question"] == "forward" for f in out))


class SelectAtoms(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c = q.load()

    def test_scope_and_ranking(self):
        out = q.select_atoms(self.c, sector="semis", since="2026-04-01", text="capacity constraint", k=8)
        self.assertEqual(len(out), 8)
        self.assertTrue(all(a["sector"] == "semis" and a["call_date"] >= "2026-04-01" for a in out))

    def test_atoms_carry_descriptions(self):
        text = q.format_atoms(q.select_atoms(self.c, text="capex", k=5))
        self.assertIn(" — ", text)
        self.assertGreater(len(text), 800)  # descriptions, not just names


class ThemeDigest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c = q.load()
        cls.themes = q.theme_digest(cls.c, top=25)

    def test_cross_company_rule(self):
        self.assertTrue(self.themes)
        self.assertTrue(all(t["n_tickers"] >= 3 for t in self.themes))

    def test_quarters_and_trend_fields(self):
        for t in self.themes:
            self.assertEqual(sorted(t["per_quarter"]), self.c["quarters"])
            self.assertIn(t["trend"], {"emerging", "rising", "fading", "steady"})
            self.assertEqual(t["n_claims"], sum(t["per_quarter"].values()))

    def test_sector_scope_restricts_members(self):
        scoped = q.theme_digest(self.c, sector="semis", top=10)
        full = {t["id"]: t for t in q.theme_digest(self.c, top=1000)}
        for t in scoped:
            self.assertLessEqual(t["n_claims"], full[t["id"]]["n_claims"])

    def test_until_scope_shrinks_or_holds_counts(self):
        early = q.theme_digest(self.c, until="2026-01-01", top=1000)
        full = {t["id"]: t for t in q.theme_digest(self.c, top=1000)}
        for t in early:
            self.assertLessEqual(t["n_claims"], full[t["id"]]["n_claims"])

    def test_format_themes_renders(self):
        text = q.format_themes(self.themes[:3])
        self.assertIn("[THEME", text)
        self.assertIn("companies", text)
        for t in self.themes[:3]:  # LLM title when present, else the flagged medoid label
            self.assertIn(t["title"] if t.get("title") else "one company's wording", text)

    def test_samples_are_distinct_companies_with_substance(self):
        for t in self.themes[:10]:
            tickers = [s.split()[0] for s in t["samples"]]
            self.assertEqual(len(tickers), len(set(tickers)))
            self.assertTrue(all(" — " in s and len(s) > 60 for s in t["samples"]))


class ParsePlan(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c = q.load()

    def test_valid_plan(self):
        p = q.parse_plan('{"symbols": ["nvda", "AMD"], "sector": "semis", "since": "2026-01-01", '
                         '"questions": ["scarcity"], "mode": "themes", "text": "capex"}', self.c)
        self.assertEqual(p["symbols"], ["NVDA", "AMD"])
        self.assertEqual(p["sector"], "semis")
        self.assertEqual(p["since"], "2026-01-01")
        self.assertEqual(p["questions"], ["scarcity"])
        self.assertEqual(p["mode"], "themes")
        self.assertEqual(p["text"], "capex")

    def test_json_with_prose_wrapper(self):
        p = q.parse_plan('Here you go:\n{"mode": "themes", "text": "ai"}\nDone.', self.c)
        self.assertEqual(p["mode"], "themes")

    def test_malformed_degrades_to_default(self):
        for bad in ("", None, "not json", '{"broken": ', '["a list"]'):
            self.assertEqual(q.parse_plan(bad, self.c), q.PLAN_DEFAULT)

    def test_invalid_values_dropped_field_by_field(self):
        p = q.parse_plan('{"symbols": ["OK", "way too long ticker", 42], "sector": "crypto", '
                         '"since": "January", "questions": ["nope"], "mode": "destroy"}', self.c)
        self.assertEqual(p["symbols"], ["OK"])
        self.assertIsNone(p["sector"])
        self.assertIsNone(p["since"])
        self.assertIsNone(p["questions"])
        self.assertEqual(p["mode"], "lookup")


if __name__ == "__main__":
    unittest.main()
