# File: agents/scoring_agent.py

class ScoringAgent:
    """
    Assigns severity, confidence, and impact scores
    """

    def score(self, findings):
        scored = []

        for f in findings:
            confidence = 0.9 if f["severity"] == "High" else 0.6
            impact = "High" if f["severity"] == "High" else "Low"

            f.update({
                "confidence": confidence,
                "financial_impact": impact
            })
            scored.append(f)

        return scored
