from app.services.ai_provider import AIProvider


class AIService:

    def __init__(self, provider: AIProvider):
        self.provider = provider

    async def generate_response(self, user_message: str) -> str:
        return await self.provider.generate_response(user_message)

    async def close(self):
        close = getattr(self.provider, "close", None)

        if close is not None:
            await close()