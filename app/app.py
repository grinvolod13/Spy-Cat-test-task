from fastapi import FastAPI
from app.view.mission import router as mission
from app.view.cat import router as cat


app = FastAPI()
app.include_router(mission, prefix='/mission')
app.include_router(cat, prefix='/cat')