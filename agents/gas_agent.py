# File: agents/gas_agent.py

class GasOptimizationAgent:
    """
    Detects gas inefficiencies
    """

    def analyze(self, source_code):
        findings = []

        if "for (" in source_code and "storage" in source_code:
            findings.append({
                "name": "Inefficient Loop",
                "description": "Loop using storage variables increases gas cost",
                "severity": "Low"
            })

        if source_code.count("uint") > 10:
            findings.append({
                "name": "Redundant Variables",
                "description": "Too many state variables increase deployment cost",
                "severity": "Low"
            })

        return findings
