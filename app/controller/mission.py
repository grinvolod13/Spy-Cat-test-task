from sqlalchemy import literal
from app.model.models import Cat, Mission, Target
from app.model.validation import Cat as CatPydantic, Targets as TargetsPydantic, UpdatedTargets
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
    
    def remove(self, id: int):
        mission = self.__get_mission(id)
        if mission.cat:
            raise OperationNotAllowedException("Can't cancel mission, it's started!")
        self.db.delete(mission)
        self.db.commit()
    
    def update_info(self, id: int, targets_: UpdatedTargets):
        mission = self.__get_mission(id)
        if mission.complete:
            raise OperationNotAllowedException("Mission completed, can't update!")
        if mission.cat is None:
            raise OperationNotAllowedException(
                "Dear Unknown Cat, ask HR to assign you first please!"
                ) # only assigned missions can have updating targets
        for upd in targets_.root:
            target = self.db.query(Target).filter(
                Target.mission_id==id,
                Target.country==upd.country,
                Target.name==upd.name,
            ).one_or_none()
            if not target:
                raise ResourseNotFoundException(
                    "This target does not exist for this mission."
                )
            if target.complete:
                raise OperationNotAllowedException(
                    "Updating notes of complete targets are not allowed."
                )
            target.notes = upd.notes
            target.complete = upd.complete
        
        self.db.flush()
        exists_not_completed = self.db.query(literal(True)).filter(self.db.query(Target).filter(
            Target.mission_id==id,
            Target.complete==False,
            ).exists()).scalar()
        if not exists_not_completed:
            mission.complete = True
        self.db.commit()
        
                
            
            
        
        
        
        