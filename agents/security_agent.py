# File: agents/security_agent.py

class SecurityAgent:
    """
    Detects common smart contract security vulnerabilities
    """

    def analyze(self, source_code):
        findings = []

        if "call.value" in source_code or ".call{" in source_code:
            findings.append({
                "name": "Reentrancy",
                "lines": "Potential external call",
                "description": "External call before state update allows reentrancy",
                "severity": "High"
            })

        if "uint" in source_code and "+" in source_code:
            findings.append({
                "name": "Integer Overflow",
                "lines": "Arithmetic operation",
                "description": "Unchecked arithmetic may overflow",
                "severity": "Medium"
            })

        if "onlyOwner" not in source_code:
            findings.append({
                "name": "Missing Access Control",
                "lines": "Critical functions",
                "description": "No access control modifier detected",
                "severity": "High"
            })

        return findings
