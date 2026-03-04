from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.champion_model import ChampionDBModel, ChampionCreateModel
from app.services.db_connection import get_db

router = APIRouter(
    prefix="/champions",
    tags=["champions"]
)

# create champion
@router.post("/", response_model=ChampionCreateModel)
def create_champion(champion: ChampionCreateModel, db: Session = Depends(get_db)):
    db_champion = ChampionDBModel(name=champion.name, lore=champion.lore, quotes=champion.quotes)
    db.add(db_champion)
    db.commit()
    db.refresh(db_champion)
    return champion

# get champion by name
@router.get("/{name}", response_model=ChampionCreateModel)
def get_champion(name: str, db: Session = Depends(get_db)):
    db_champion = db.query(ChampionDBModel).filter(ChampionDBModel.name == name).first()
    if db_champion is None:
        raise HTTPException(status_code=404, detail="Champion not found")
    return ChampionCreateModel(name=db_champion.name, lore=db_champion.lore, quotes=db_champion.quotes)

# get all champions
@router.get("/", response_model=list[ChampionCreateModel])
def get_all_champions(db: Session = Depends(get_db)):
    db_champions = db.query(ChampionDBModel).all()
    return [ChampionCreateModel(name=champ.name, lore=champ.lore, quotes=champ.quotes) for champ in db_champions]

# update champion by name
@router.put("/{name}", response_model=ChampionCreateModel)
def update_champion(name: str, champion: ChampionCreateModel, db: Session = Depends(get_db)):
    db_champion = db.query(ChampionDBModel).filter(ChampionDBModel.name == name).first()
    if db_champion is None:
        raise HTTPException(status_code=404, detail="Champion not found")
    db_champion.name = champion.name
    db_champion.lore = champion.lore
    db_champion.quotes = champion.quotes
    db.commit()
    return champion

# delete champion by name
@router.delete("/{name}")
def delete_champion(name: str, db: Session = Depends(get_db)):
    db_champion = db.query(ChampionDBModel).filter(ChampionDBModel.name == name).first()
    if db_champion is None:
        raise HTTPException(status_code=404, detail="Champion not found")
    db.delete(db_champion)
    db.commit()
    return {"detail": "Champion deleted"}
