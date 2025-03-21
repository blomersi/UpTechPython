from fastapi import FastAPI


app = FastAPI(title="Minha Aplicação UpTechPython")


@app.get("/")
def read_root():
    return {"Hello": "World"}
