class CoordinatorAgent:
    """
    Coordinates all agents and merges insights
    """

    def coordinate(self, security_findings, gas_findings, compliance_findings):
        combined = []

        for f in security_findings + gas_findings + compliance_findings:
            # Cross-agent enrichment
            if f["name"] == "Reentrancy":
                f["impact_detail"] = "May lead to complete fund drain"

            combined.append(f)

        return combined