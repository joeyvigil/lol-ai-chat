from fastapi import FastAPI
from app.routers import champion_router, langchain_ops
from app.services.db_connection import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

# REGISTER my routers (so they actually show up in SwaggerUI)
# app.include_router(dino_router.router)
app.include_router(champion_router.router)
app.include_router(langchain_ops.router)

# Generic sample endpoint (greeting GET request)
@app.get("/")
async def sample_endpoint():
    return {"message":"Hello from the League of Legends AI Chat API! Visit /docs for the API documentation."}