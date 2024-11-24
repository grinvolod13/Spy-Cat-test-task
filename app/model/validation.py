from pydantic import BaseModel, RootModel, Field
from annotated_types import Len, Ge
from typing import List, Annotated



class Target(BaseModel):
    name: str
    country: str

class UpdatedTarget(BaseModel):
    name: str
    country: str
    notes: str = ""
    complete: bool = False
    

class Targets(RootModel):
    root: Annotated[List[Target], Len(1, 3)]
    
class UpdatedTargets(RootModel):
    root: Annotated[List[UpdatedTarget], Len(1, 3)]
    
Salary = Annotated[float, Ge(0)]

class Cat(BaseModel):
    name: str
    years_of_expirience: Annotated[float, Ge(0)] # i belive number like 1.5 yrs should be valid in CVs
    breed: str
    salary: Salary