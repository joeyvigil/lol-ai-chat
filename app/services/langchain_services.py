from langchain_classic.chains.conversation.base import ConversationChain
from langchain_classic.memory import ConversationBufferWindowMemory
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2:3b", # The model we're using
    temperature=0.5 # Temp goes from 0-1. Higher temp = more creative responses from the LLM
)

prompt = ChatPromptTemplate.from_messages([
    ("system",
     """You are a league of legends champion chat bot. You answer questions about league of legends, the champions, the lore, and general game mechanics.
    You speak like the champion you are, and you answer questions in character."""),
    ("user", "{input}")
])

def get_basic_chain():
    chain = prompt | llm
    return chain 


def get_sequential_chain():
    draft_chain = prompt | llm
    refined_prompt = ChatPromptTemplate.from_messages([
        ("system",
         """The user has given you some feedback on your previous response. Use that feedback to refine your answer.
         You are a league of legends champion chat bot. You answer questions about league of legends, the champions, the lore, and general game mechanics.
         You speak like the champion you are, and you answer questions in character."""),
        ("user", "{input}")
    ])

    refined_chain = refined_prompt | llm
    sequential_chain = draft_chain | refined_chain
    return sequential_chain

# A Chain that stores memory so it can recall what was being talked about
def get_memory_chain():
    # This Memory instance remembers the last "k" interactions
    memory = ConversationBufferWindowMemory(k=10)
    memory_prompt = ChatPromptTemplate.from_messages([
        ("system",
         """You are a league of legends champion chat bot. You answer questions about league of legends, the champions, the lore, and general game mechanics.
        You speak like the champion you are, and you answer questions in character."""),
        ("user", "Current input: {input},"
                 "Conversation history: {history}")
    ])

    memory_chain = ConversationChain(
        llm = llm,
        memory = memory,
        prompt = memory_prompt
    )

    memory_chain = ConversationChain(
        llm = llm,
        memory = memory,
        prompt = memory_prompt
    )

    return memory_chain