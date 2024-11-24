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
        
    
    def get_all(self):
        return self.db.query(Mission).all()
    
    
    def get(self, id):
        mission = self.db.query(Mission).filter(Mission.id==id).one_or_none()
        if not mission:
            raise ResourseNotFoundException(f"Mission with id: {id} does not exists")
        return mission
    
    
    
    # def remove(self, id: int):
    #     cat = self.db.query(Cat).filter(Cat.id==id).one_or_none()
    #     if not cat:
    #         raise ValueError(f"Cat with id: {id} does not exists")
    #     self.db.delete(cat)
    #     self.db.commit()

        
        
    # def set_salary(self, id: int, salary: Salary):
    #     count = self.db.query(Cat).filter(Cat.id==id).update({Cat.salary: salary})
    #     self.db.commit()
    #     if not count:
    #         raise ValueError(f"Cat with id: {id} does not exists")
        