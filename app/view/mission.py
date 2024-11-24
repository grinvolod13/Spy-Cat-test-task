from fastapi.routing import APIRouter

from app.dependency import DB
from app.model import Mission, Target
from app.model import Targets # validation pydantic model 

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

@router.put('/{id}/{cat_id}')
def assign_cat(id: int, cat_id: int, db: DB):
    ...
    
@router.put('/{id}')
def update_targets(id: int, targets: Targets, db: DB):
    ...

@router.post('/')
def new_mission():
    ...
