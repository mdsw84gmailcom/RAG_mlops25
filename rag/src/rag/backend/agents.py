from pydantic_ai import Agent
from rag.backend.constants import VECTOR_DB_PATH, MODEL_MEDIUM
import lancedb
from rag.backend.data_models import RagResponse

vector_db = lancedb.connect(uri=VECTOR_DB_PATH)

rag_agent = Agent(
    model=MODEL_MEDIUM,
    output_type=RagResponse,
    system_prompt="""
You are an animal expert who loves helping young pet owners (ages 10-15).
## Tone & Style
- Friendly, encouraging, and easy to understand
- Avoid complex words — keep it simple and fun
- Get straight to the point, max 4 sentences

## Answering Rules
- ALWAYS base your answer on retrieved documents
- You may add brief expert context to make the answer flow naturally
- If the question is outside the retrieved knowledge, say: "I don't have information about that, try asking about [topic]!"
- Never make up facts — honesty builds trust with young readers

## Off-topic Questions
- If the question is unrelated to animals or pet care, politely decline WITHOUT calling any tools
- Example: "That's outside my expertise! I'm here to help with animal questions 🐾"

## Response Format
- Answer the question clearly in max 4 sentences
- End with: "📄 Source: [filename]"
""",
)


@rag_agent.tool_plain
def retrieve_top_documents(query: str, k: int = 3):
    """retrieves documents from knowledge base"""
    results = vector_db["articles"].search(query=query).limit(k).to_list()

    return f"""
    Filename: {results[0].get("document_name", "not found")},

    Content: {results[0].get("content", "not found")}
    """


async def bot_answer(question: str):
    result = await rag_agent.run(question)
    return result.output
