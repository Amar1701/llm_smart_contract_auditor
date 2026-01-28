# File: agents/report_agent.py

import markdown

class ReportAgent:
    """
    Generates final Markdown audit report
    """

    def generate(self, findings, output_path):
        report = "# Smart Contract Audit Report\n\n"

        for f in findings:
            report += f"""
## {f['name']}
- **Severity:** {f['severity']}
- **Confidence:** {f['confidence']}
- **Financial Impact:** {f['financial_impact']}

**Description:**  
{f['description']}

---
"""

        with open(output_path, "w") as file:
            file.write(report)
