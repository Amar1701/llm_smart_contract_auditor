class ScoringAgent:

    def score(self, findings):
        for f in findings:

            severity_weight = {
                "High": 0.9,
                "Medium": 0.6,
                "Low": 0.3
            }

            base = severity_weight.get(f["severity"], 0.5)

            # Increase confidence if critical keywords
            if "fund" in f.get("description", "").lower():
                base += 0.1

            f["confidence"] = round(min(base, 1.0), 2)

            # Financial impact logic
            if f["severity"] == "High":
                f["financial_impact"] = "Critical"
            else:
                f["financial_impact"] = "Moderate"

        return findings