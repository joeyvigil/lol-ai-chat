from fastapi import APIRouter
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel

# from app.models.champion_model import Champion
# from langchain_core.chains import ConversationChain
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

@router.post("/basic")
async def basic_chain_endpoint(input: ChatInputModel):
    response = basic_chain(input.input)
    return {"response": response}