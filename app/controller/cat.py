
from app.model.models import Cat
from app.model.validation import Cat as CatPydantic, Salary
from sqlalchemy.orm import Session
from app.exceptions import *

class CatController:
    def __init__(self, db: Session) -> None:
        self.db = db
        
    def get_all(self):
        return self.db.query(Cat).all()
    
    def get(self, id):
        cat = self.db.query(Cat).filter(Cat.id==id).one_or_none()
        if not cat:
            raise ResourseNotFoundException(f"Cat with id: {id} does not exists")
    
    def create(self, cat_: CatPydantic):
        cat = Cat(**cat_.model_dump())
        self.db.add(cat)
        self.db.commit()
        
    def remove(self, id: int):
        cat = self.db.query(Cat).filter(Cat.id==id).one_or_none()
        if not cat:
            raise ResourseNotFoundException(f"Cat with id: {id} does not exists")
        self.db.delete(cat)
        self.db.commit()

        
        
    def set_salary(self, id: int, salary: Salary):
        count = self.db.query(Cat).filter(Cat.id==id).update({Cat.salary: salary})
        self.db.commit()
        if not count:
            raise ValueError(f"Cat with id: {id} does not exists")
        