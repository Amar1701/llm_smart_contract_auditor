# File: main.py

import os
import logging

from parser.solidity_parser import SolidityParser
from agents.security_agent import SecurityAgent
from agents.gas_agent import GasOptimizationAgent
from agents.compliance_agent import ComplianceAgent
from agents.scoring_agent import ScoringAgent
from agents.report_agent import ReportAgent
from agents.coordinator_agent import CoordinatorAgent

from evaluation.slither_runner import SlitherRunner
from evaluation.metrics import EvaluationMetrics


# 🔥 LOGGING SYSTEM
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def prioritize_findings(findings):
    severity_rank = {
        "High": 3,
        "Medium": 2,
        "Low": 1
    }

    return sorted(
        findings,
        key=lambda x: severity_rank.get(x.get("severity", "Low"), 1),
        reverse=True
    )


def process_contract(contract_path):
    """
    Runs full pipeline for ONE contract
    """

    logging.info(f"Processing contract: {contract_path}")

    parser = SolidityParser()
    security = SecurityAgent()
    gas = GasOptimizationAgent()
    compliance = ComplianceAgent()
    scoring = ScoringAgent()
    report = ReportAgent()
    coordinator = CoordinatorAgent()

    slither = SlitherRunner()
    evaluator = EvaluationMetrics()

    # --- Parsing ---
    parsed = parser.parse(contract_path)

    # --- Agents ---
    security_findings = security.analyze(parsed["source"], parsed["ast"])
    gas_findings = gas.analyze(parsed["source"])
    compliance_findings = compliance.analyze(parsed["source"])

    # --- Coordination ---
    findings = coordinator.coordinate(
        security_findings,
        gas_findings,
        compliance_findings
    )

    logging.info(f"Findings before scoring: {len(findings)}")

    # --- Scoring ---
    scored = scoring.score(findings)

    # --- PRIORITIZATION ---
    prioritized = prioritize_findings(scored)

    # --- Slither ---
    slither_results = slither.run(contract_path)

    # 🔥 DEBUG LINES ADDED HERE
    print("\n🔍 Detected by our system:")
    print([f["name"] for f in prioritized])

    print("\n🔍 Detected by Slither:")
    print(slither_results)

    # --- Metrics ---
    metrics = evaluator.evaluate(prioritized, slither_results)

    logging.info(f"Metrics: {metrics}")

    # --- Report Path ---
    file_name = os.path.basename(contract_path).replace(".sol", "")
    report_path = f"reports/{file_name}_audit.md"

    # --- Report ---
    report.generate(prioritized, report_path)

    logging.info(f"Report generated: {report_path}")

    return metrics


def main():
    contracts_folder = "data/sample_contracts"

    all_metrics = []

    logging.info("Starting Batch Smart Contract Auditing...")

    # 🔥 BATCH PROCESSING
    for file in os.listdir(contracts_folder):
        if file.endswith(".sol"):
            path = os.path.join(contracts_folder, file)
            metrics = process_contract(path)
            all_metrics.append(metrics)

    # --- Overall Summary ---
    if all_metrics:
        avg_precision = sum(m["Precision"] for m in all_metrics) / len(all_metrics)
        avg_recall = sum(m["Recall"] for m in all_metrics) / len(all_metrics)

        print("\n📊 Overall Performance:")
        print(f"Average Precision: {round(avg_precision, 2)}")
        print(f"Average Recall: {round(avg_recall, 2)}")

    logging.info("Batch audit completed successfully.")


if __name__ == "__main__":
    main()