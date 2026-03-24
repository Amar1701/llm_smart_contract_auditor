# File: agents/report_agent.py

import markdown

# File: agents/report_agent.py

from llm.llm_client import LLMClient
from llm.prompts import VULNERABILITY_EXPLANATION_PROMPT

class ReportAgent:
    def __init__(self):
        self.llm = LLMClient()

    def generate(self, findings, output_path):
        report = "# Smart Contract Audit Report\n\n"

        for f in findings:
            prompt = VULNERABILITY_EXPLANATION_PROMPT.format(
                vulnerability=f["name"]
            )

            try:
                explanation = self.llm.explain(prompt)
            except:
                explanation = "LLM explanation not available"

            report += f"""
## {f['name']}

- **Severity:** {f['severity']}
- **Confidence:** {f['confidence']}
- **Financial Impact:** {f['financial_impact']}

**Technical Description:**  
{f['description']}

**LLM Explanation:**  
{explanation}

---
"""

        with open(output_path, "w") as file:
            file.write(report)