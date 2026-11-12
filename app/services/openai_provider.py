from openai import AsyncOpenAI

from app.core.config import settings


class OpenAIProvider:

    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.openai_api_key,
            timeout=30.0,
            max_retries=2,
        )

    async def generate_response(self, message: str) -> str:
        response = await self.client.responses.create(
            model=settings.openai_model,
            instructions=(
                "You are a helpful customer support assistant. "
                "Be clear, professional and honest. "
                "Never invent company policies. "
                "If you lack sufficient information, "
                "explain that you cannot verify the answer."
            ),
            input=message,
        )

        return response.output_text

    async def close(self) -> None:
        await self.client.close()
