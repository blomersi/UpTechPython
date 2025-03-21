from fastapi import APIRouter, HTTPException

from app.core import db
from app.models.jogador import JogadorModel

router = APIRouter()

collection = db.db.get_collection("jogadores")


@router.post("/")
async def create_jogador(payload: JogadorModel):
    #jogador = payload.model_dump()
    print(payload)
    result = await collection.insert_one(payload)
    

    return {"jogador": result}