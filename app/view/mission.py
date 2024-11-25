from fastapi import HTTPException
from fastapi.routing import APIRouter

from app.dependency import DB
from app.model import Targets, UpdatedTargets, Mission # validation pydantic model 
from app.model import MissionResponse

from app.controller import MissionController
router = APIRouter()


@router.get('/', response_model=list[MissionResponse])
def get_all(db: DB):
    return MissionController(db).get_all()

@router.get('/{id}', response_model=MissionResponse)
def get_single(id: int, db: DB):
    return MissionController(db).get(id)

@router.delete('/{id}')
def remove_mission(id: int, db: DB):
    MissionController(db).remove(id)
    return {'status': 'OK'}

@router.put('/{id}/{cat_id}')
def assign_cat(id: int, cat_id: int, db: DB):
    MissionController(db).assign_cat(id, cat_id)
    return {'status': 'OK'}
    
@router.put('/{id}')
def update_targets(id: int, targets: UpdatedTargets, db: DB):
    MissionController(db).update_info(id, targets)
    return {'status': 'OK'}

@router.post('/')
def new_mission(targets: Targets, db: DB):
    MissionController(db).create(targets)
    return {'status': 'OK'}
