from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import router

app = FastAPI(title="Graph Pipeline Analyzer", version="0.1.0")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(router)
