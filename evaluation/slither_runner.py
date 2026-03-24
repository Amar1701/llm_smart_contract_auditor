# File: evaluation/slither_runner.py

import subprocess
import json

class SlitherRunner:
    def run(self, contract_path):
        try:
            result = subprocess.run(
                ["slither", contract_path, "--json", "slither_output.json"],
                capture_output=True,
                text=True
            )

            with open("slither_output.json") as f:
                data = json.load(f)

            issues = []
            for detector in data.get("results", {}).get("detectors", []):
                issues.append(detector.get("check", "").lower())

            return issues

        except Exception:
            return []