from fastapi import FastAPI
from app.view.mission import router as mission


app = FastAPI()
app.include_router(mission, prefix='/mission')