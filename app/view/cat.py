from fastapi.routing import APIRouter
from fastapi import HTTPException, status
from app.dependency import DB
from app.model import Mission, Target
from app.model import Targets, UpdatedTargets, Salary, Cat # validation pydantic model
from app.const import CAT_BREED_API
from app.model import validation
from app.controller import CatController


router = APIRouter()


@router.get('/', response_model=list[Cat])
def get_all(db: DB):
    return CatController(db).get_all()

@router.get('/{id}', response_model=Cat)
def get_single(id: int, db: DB):
    return CatController(db).get(id)

        

@router.delete('/{id}')
def fire_cat(id: int, db: DB):
    CatController(db).remove(id)

@router.put('/{id}/')
def update_salary(id: int, salary: Salary, db: DB):
    CatController(db).set_salary(id, salary)

@router.post('/')
async def add_cat(cat: Cat, db: DB):
    if not (await validation.validate_breed(cat)):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Unknown breed, check out {CAT_BREED_API} for correct breed names",
            )
    return CatController(db).create(cat)
    
