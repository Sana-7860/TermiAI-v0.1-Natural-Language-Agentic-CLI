# LLM Layer - Provider Abstraction
# Owner: Sana-7860 - Workstream 6

class LLMProvider:
    def __init__(self, provider="openai", model="gpt-4"):
        self.provider = provider
        self.model = model

    def get_response(self, prompt: str) -> str:
        if self.provider == "openai":
            return f"[Cloud:{self.model}] Response for: {prompt}"
        else:
            return f"[Local:{self.model}] Response for: {prompt}"

def get_provider(config):
    return LLMProvider(
        provider=config.get("provider", "openai"),
        model=config.get("model", "gpt-4")
    )
