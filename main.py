# File: main.py

from parser.solidity_parser import SolidityParser
from agents.security_agent import SecurityAgent
from agents.gas_agent import GasOptimizationAgent
from agents.compliance_agent import ComplianceAgent
from agents.scoring_agent import ScoringAgent
from agents.report_agent import ReportAgent

def main():
    parser = SolidityParser()
    parsed = parser.parse("data/sample_contracts/vulnerable_contract.sol")

    security = SecurityAgent()
    gas = GasOptimizationAgent()
    compliance = ComplianceAgent()
    scoring = ScoringAgent()
    report = ReportAgent()

    findings = []
    findings += security.analyze(parsed["source"])
    findings += gas.analyze(parsed["source"])
    findings += compliance.analyze(parsed["source"])

    scored = scoring.score(findings)
    report.generate(scored, "reports/sample_audit_report.md")

    print("Audit completed successfully.")

if __name__ == "__main__":
    main()
