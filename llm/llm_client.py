# File: llm/llm_client.py

class LLMClient:
    """
    Mock LLM (No API required)
    Used for explanation and reasoning simulation
    """

    def explain(self, prompt):
        return (
            "This vulnerability occurs due to unsafe smart contract logic. "
            "It can lead to financial loss or unauthorized access. "
            "Recommended fix: follow secure coding practices such as checks-effects-interactions pattern."
        )