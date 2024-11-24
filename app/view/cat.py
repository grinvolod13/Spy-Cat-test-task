from fastapi.routing import APIRouter

from app.dependency import DB
from app.model import Mission, Target
from app.model import Targets, UpdatedTargets, Salary, Cat # validation pydantic model

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
def add_cat(cat: Cat):
    ...
