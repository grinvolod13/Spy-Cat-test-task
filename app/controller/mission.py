from app.model.models import Cat, Mission, Target
from app.model.validation import Cat as CatPydantic, Targets as TargetsPydantic
from sqlalchemy.orm import Session

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
        
    