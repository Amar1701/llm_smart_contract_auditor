# File: agents/compliance_agent.py

class ComplianceAgent:
    """
    Checks ERC20 / ERC721 compliance
    """

    REQUIRED_ERC20_FUNCTIONS = ["transfer", "balanceOf", "approve"]

    def analyze(self, source_code):
        findings = []

        for func in self.REQUIRED_ERC20_FUNCTIONS:
            if func not in source_code:
                findings.append({
                    "name": "ERC20 Non-Compliance",
                    "description": f"Missing required function: {func}",
                    "severity": "Medium"
                })

        return findings
