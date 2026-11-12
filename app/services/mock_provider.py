class MockProvider:

    async def generate_response(self, message: str) -> str:
        return (
            f"This is a simulated AI response. "
            f"You asked: {message}"
        )