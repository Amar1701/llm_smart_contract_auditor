# File: agents/compliance_agent.py

class ComplianceAgent:
    def analyze(self, source_code):
        findings = []

        # Only check if it's clearly a token
        if "transfer(" in source_code or "balanceOf(" in source_code:
            missing = []

            required = ["transfer", "balanceOf", "approve"]

            for func in required:
                if func not in source_code:
                    missing.append(func)

            if missing:
                findings.append({
                    "name": "ERC20 Compliance Issue",
                    "description": f"Missing: {', '.join(missing)}",
                    "severity": "Medium"
                })

        return findings