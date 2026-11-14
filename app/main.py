from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from openai import OpenAIError
from pydantic import BaseModel, Field

from app.services.ai_service import AIService
from app.services.mock_provider import MockProvider


ai_service = AIService(
    provider=MockProvider()
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await ai_service.close()


app = FastAPI(
    title="Conversiq",
    description="An AI-powered customer support platform",
    version="0.1.0",
    lifespan=lifespan,
)


class ChatRequest(BaseModel):
    message: str = Field(
        min_length=1,
        max_length=4000,
    )


class ChatResponse(BaseModel):
    answer: str


@app.get("/")
async def root():
    return {
        "message": "AI Customer Support API is running",
        "status": "healthy"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.post("/api/v1/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    try:
        answer = await ai_service.generate_response(
            request.message
        )

        return ChatResponse(answer=answer)

    except OpenAIError as exc:
        print(f"AI provider error: {type(exc).__name__}: {exc}")

        raise HTTPException(
            status_code=502,
            detail="The AI provider could not process your request.",
        ) from exc