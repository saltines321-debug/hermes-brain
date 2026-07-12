import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import brain


class BrainMemoryTests(unittest.TestCase):
    def test_run_cycle_writes_memory_outcome(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            inbox_dir = root / "inbox"
            inbox_dir.mkdir(parents=True)
            (inbox_dir / "sample.json").write_text(
                json.dumps({"kind": "example"}),
                encoding="utf-8",
            )

            policies_dir = root / "policies"
            policies_dir.mkdir(parents=True)
            (policies_dir / "runtime_rules.json").write_text(
                json.dumps({"risk_score": 0.0, "max_iterations": 1}),
                encoding="utf-8",
            )
            (policies_dir / "privacy.json").write_text(
                json.dumps({"local_first": True}),
                encoding="utf-8",
            )

            memory_dir = root / "memory"
            memory_dir.mkdir(parents=True)
            outbox_dir = root / "outbox"
            outbox_dir.mkdir(parents=True)

            with mock.patch.object(brain, "ROOT", root), mock.patch.object(
                brain, "POLICY_DIR", policies_dir
            ), mock.patch.object(brain, "INBOX_DIR", inbox_dir), mock.patch.object(
                brain, "OUTBOX_DIR", outbox_dir
            ), mock.patch.object(brain, "MEMORY_DIR", memory_dir, create=True):
                decisions = brain.run_cycle()

            self.assertEqual(len(decisions), 1)
            memory_path = memory_dir / "outcomes.jsonl"
            self.assertTrue(memory_path.exists())
            lines = [line for line in memory_path.read_text(encoding="utf-8").splitlines() if line.strip()]
            self.assertEqual(len(lines), 1)
            entry = json.loads(lines[0])
            self.assertEqual(entry["item"], "sample.json")
            self.assertEqual(entry["risk_score"], 0.0)
            self.assertIn("status", entry)
            self.assertIn("intent", entry)
            self.assertIn("mode", entry)

    def test_read_recent_outcomes_ignores_meta_entries(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            memory_dir = root / "memory"
            memory_dir.mkdir(parents=True)
            memory_path = memory_dir / "outcomes.jsonl"
            memory_path.write_text(
                json.dumps({"_note": "meta"}) + "\n" + json.dumps({"item": "sample.json"}) + "\n",
                encoding="utf-8",
            )

            with mock.patch.object(brain, "MEMORY_DIR", memory_dir, create=True):
                entries = brain.read_recent_outcomes(limit=10)

            self.assertEqual(len(entries), 1)
            self.assertEqual(entries[0]["item"], "sample.json")

    def test_run_cycle_skips_memory_when_disabled(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            inbox_dir = root / "inbox"
            inbox_dir.mkdir(parents=True)
            (inbox_dir / "sample.json").write_text(
                json.dumps({"kind": "example"}),
                encoding="utf-8",
            )

            policies_dir = root / "policies"
            policies_dir.mkdir(parents=True)
            (policies_dir / "runtime_rules.json").write_text(
                json.dumps({"risk_score": 0.0, "max_iterations": 1, "memory_enabled": False}),
                encoding="utf-8",
            )
            (policies_dir / "privacy.json").write_text(
                json.dumps({"local_first": True}),
                encoding="utf-8",
            )

            memory_dir = root / "memory"
            memory_dir.mkdir(parents=True)
            outbox_dir = root / "outbox"
            outbox_dir.mkdir(parents=True)

            with mock.patch.object(brain, "ROOT", root), mock.patch.object(
                brain, "POLICY_DIR", policies_dir
            ), mock.patch.object(brain, "INBOX_DIR", inbox_dir), mock.patch.object(
                brain, "OUTBOX_DIR", outbox_dir
            ), mock.patch.object(brain, "MEMORY_DIR", memory_dir, create=True):
                decisions = brain.run_cycle()

            self.assertEqual(len(decisions), 1)
            self.assertFalse((memory_dir / "outcomes.jsonl").exists())

    def test_run_cycle_supports_dry_run_mode(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            inbox_dir = root / "inbox"
            inbox_dir.mkdir(parents=True)
            (inbox_dir / "sample.json").write_text(
                json.dumps({"kind": "example"}),
                encoding="utf-8",
            )

            policies_dir = root / "policies"
            policies_dir.mkdir(parents=True)
            (policies_dir / "runtime_rules.json").write_text(
                json.dumps({"risk_score": 0.0, "max_iterations": 1, "default_mode": "dry_run"}),
                encoding="utf-8",
            )
            (policies_dir / "privacy.json").write_text(
                json.dumps({"local_first": True}),
                encoding="utf-8",
            )

            memory_dir = root / "memory"
            memory_dir.mkdir(parents=True)
            outbox_dir = root / "outbox"
            outbox_dir.mkdir(parents=True)

            with mock.patch.object(brain, "ROOT", root), mock.patch.object(
                brain, "POLICY_DIR", policies_dir
            ), mock.patch.object(brain, "INBOX_DIR", inbox_dir), mock.patch.object(
                brain, "OUTBOX_DIR", outbox_dir
            ), mock.patch.object(brain, "MEMORY_DIR", memory_dir, create=True):
                decisions = brain.run_cycle()

            self.assertEqual(len(decisions), 1)
            self.assertEqual(decisions[0]["mode"], "dry_run")
            self.assertEqual(decisions[0]["action"]["status"], "skipped")


if __name__ == "__main__":
    unittest.main()
