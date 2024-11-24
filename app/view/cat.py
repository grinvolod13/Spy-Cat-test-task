from fastapi.routing import APIRouter
from fastapi import HTTPException, status
from app.dependency import DB
from app.model import Mission, Target
from app.model import Targets, UpdatedTargets, Salary, Cat # validation pydantic model
from app.const import CAT_BREED_API
from app.model import validation

router = APIRouter()


@router.get('/')
def get_all(db: DB):
    ...

@router.get('/{id}')
def get_single(id: int, db: DB):
    ...

@router.delete('/{id}')
def remove_mission(id: int, db: DB):
    ...

@router.put('/{id}/')
def update_salary(id: int, salary: Salary, db: DB):
    ...

@router.post('/')
async def add_cat(cat: Cat):
    if not (await validation.validate_breed(cat)):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Unknown breed, check out {CAT_BREED_API} for correct breed names",
            )
    
