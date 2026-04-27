from fastapi import FastAPI
from rag.backend.agents import bot_answer
from rag.backend.data_models import Prompt, RagResponse

app = FastAPI()


@app.post("/rag/query")
async def query_documentation(query: Prompt) -> RagResponse:
    result = await bot_answer(query.prompt)

    return result
