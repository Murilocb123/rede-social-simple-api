from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json

app = FastAPI()

with open("data/feed_fotos.json", "r", encoding="utf-8") as f:
    feed_fotos = json.load(f)

@app.get("/status")
def get_status():
    return {"status": "API em funcionamento"}

@app.get("/feed_fotos")
def get_feed_fotos():
    return JSONResponse(content=feed_fotos)