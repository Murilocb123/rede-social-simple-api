from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json

app = FastAPI()

with open("data/fotos.json", "r", encoding="utf-8") as f:
    fotos = json.load(f)

@app.get("/status")
def status():
    return {"status": "API em funcionamento"}

@app.get("/fotos")
def get_fotos():
    return JSONResponse(content=fotos)