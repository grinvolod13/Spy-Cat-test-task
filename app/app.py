from fastapi import FastAPI, HTTPException, Request
from app.view.mission import router as mission
from app.view.cat import router as cat

from app.exceptions import *

app = FastAPI()

# Routers
app.include_router(mission, prefix='/mission')
app.include_router(cat, prefix='/cat')




# handelrs for custom exceptions (look in app.exceptions)

@app.exception_handler(ResourseNotFoundException)
def resourse_not_found(request: Request, e: ResourseNotFoundException):
    raise HTTPException(status_code=404, detail=e.args[0])

@app.exception_handler(ValueErrorException)
def resourse_not_found(request: Request, e: ValueErrorException):
    raise HTTPException(status_code=422, detail=e.args[0])

@app.exception_handler(OperationNotAllowedException)
def resourse_not_found(request: Request, e: OperationNotAllowedException):
    raise HTTPException(status_code=405, detail=e.args[0])