# File: llm/prompts.py

VULNERABILITY_EXPLANATION_PROMPT = """
Explain the following smart contract vulnerability in simple terms:

Vulnerability: {vulnerability}

Also provide:
1. Why it is dangerous
2. Real-world impact
3. Suggested fix
"""

SMART_ANALYSIS_PROMPT = """
Analyze the following Solidity smart contract and identify vulnerabilities:

Code:
{code}

Return:
- Vulnerability name
- Explanation
- Suggested fix
"""