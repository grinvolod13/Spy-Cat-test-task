from app.model.models import Cat, Mission, Target
from app.model.validation import Cat as CatPydantic, Targets as TargetsPydantic
from sqlalchemy.orm import Session
from app.exceptions import *


class MissionController:
    def __init__(self, db: Session) -> None:
        self.db = db
        
    def create(self, targets_: TargetsPydantic):
        with self.db.begin_nested() as db:
            mission = Mission()
            self.db.add(mission)
            self.db.flush()
            targets = [Target(mission_id=mission.id, **(tg.model_dump())) for tg in targets_.root]
            self.db.add_all(targets)
            self.db.commit()
        
    def __get_cat(self, id: int)-> Cat:
        cat = self.db.query(Cat).filter(Cat.id==id).one_or_none()
        if not cat:
            raise ResourseNotFoundException(f"Cat with id: {id} does not exists")
        return cat
        
        
    def __get_mission(self, id: int)-> Mission:
        mission = self.db.query(Mission).filter(Mission.id==id).one_or_none()
        if not mission:
            raise ResourseNotFoundException(f"Mission with id: {id} does not exists")
        return mission
    
    def get_all(self):
        return self.db.query(Mission).all()
    
    def get(self, id):
        mission = self.__get_mission(id)
        return mission
    
    def assign_cat(self, id: int, cat_id: int):
        mission = self.__get_mission(id)
        cat = self.__get_cat(cat_id)
        
        if mission.cat:
            raise OperationNotAllowedException(f"This mission (id: {mission.id}) already have assigned Spy-Cat!")
        active_missions = self.db.query(Mission).filter(Mission.complete==False, Mission.cat_id==cat_id).one_or_none()
        if active_missions:
            raise OperationNotAllowedException(f"This cat (id: {cat.id}) already have mission, use another Spy-Cat!")
        
        mission.cat_id = cat.id
        self.db.commit()
        
        
        