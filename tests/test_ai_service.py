from app.services.ai_service import AIService


class MockAIProvider:
    async def generate_response(self, message: str) -> str:
        return f"Mock response to: {message}"


async def test_ai_service_uses_provider():
    provider = MockAIProvider()
    service = AIService(provider=provider)

    result = await service.generate_response("Hello")
    assert result == "Mock response to: Hello"