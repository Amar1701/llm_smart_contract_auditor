# File: llm/llm_client.py

from langchain.llms import OpenAI

class LLMClient:
    def __init__(self):
        self.llm = OpenAI(temperature=0)

    def explain(self, prompt):
        return self.llm(prompt)
