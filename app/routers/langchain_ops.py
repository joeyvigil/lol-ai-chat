from fastapi import APIRouter
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel

# from app.models.champion_model import Champion
from app.services.langchain_services import get_basic_chain, get_sequential_chain, get_memory_chain

# Same old router setup
router = APIRouter(
    prefix="/langchain",
    tags=["langchain"]
)

class ChatInputModel(BaseModel):
    input: str
    
basic_chain = get_basic_chain()
refined_answer_chain = get_sequential_chain()
memory_chain = get_memory_chain()

@router.post("/chat")
async def general_chat(chat:ChatInputModel):
    return basic_chain.invoke({"input": chat.input})

@router.post("/memory-chat")
async def memory_chat(chat:ChatInputModel):
    return memory_chain.invoke({"input": chat.input})

# clear memory chat endpoint
@router.post("/clear-memory")
async def clear_memory():
    memory_chain.memory.clear()
    return {"message": "Memory cleared!"}