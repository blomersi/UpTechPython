from fastapi import FastAPI
from app.api.routes.jogadores import router as jogadores


app = FastAPI(title="Minha Aplicação UpTechPython")

app.include_router(jogadores, prefix="/jogadores", tags=["jogadores"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
