from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

from app.services.db_connection import Base

class ChampionDBModel(Base):
    __tablename__ = "champions"

    # Define the columns, complete with constraints
    id = Column(Integer, primary_key=True) # Setting primary_key = True makes this autoincrement!
    name = Column(String, unique=True, nullable=False)
    lore = Column(String, nullable=False)
    quotes = Column(String, nullable=False)
    
class ChampionCreateModel(BaseModel):
    name: str
    lore: str
    quotes: str



