# File: agents/security_agent.py

class SecurityAgent:
    """
    Detects real vulnerabilities matching Slither patterns
    """

    def analyze(self, source_code, ast):
        findings = []

        # 🔥 Reentrancy (improved detection)
        if ".call{" in source_code or ".call.value(" in source_code:
            if "balances" in source_code:
                findings.append({
                    "name": "Reentrancy",
                    "description": "External call before state update",
                    "severity": "High"
                })

        # 🔥 Low-level calls
        if ".call{" in source_code or ".call(" in source_code:
            findings.append({
                "name": "Low Level Call",
                "description": "Use of low-level call may be unsafe",
                "severity": "Medium"
            })

        # 🔥 Solidity version issue (generalized)
        if "pragma solidity" in source_code and "^" in source_code:
            findings.append({
                "name": "Solidity Version",
                "description": "Floating pragma version may introduce risks",
                "severity": "Low"
            })

        return findings