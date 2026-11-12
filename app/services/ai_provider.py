from typing import Protocol


class AIProvider(Protocol):

    async def generate_response(self, message: str) -> str:
        ...