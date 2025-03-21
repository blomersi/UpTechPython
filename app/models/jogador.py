from bson import ObjectId
from pydantic import BaseModel, Field

class JogadorModel(BaseModel):
    nome: str = Field(..., title="Nome do jogador", description="Nome do jogador", max_length=100)
    idade: int = Field(..., title="Idade do jogador", description="Idade do jogador", ge=0)
    posicao: str = Field(..., title="Posição do jogador", description="Posição do jogador", max_length=100)
    nacionalidade: str = Field(..., title="Nacionalidade do jogador", description="Nacionalidade do jogador", max_length=100)
    time_associado: str = Field(..., title="Time do jogador", description="Time do jogador", max_length=100)
    salario: str = Field(..., title="Salário do jogador", description="Salário do jogador", max_length=100)