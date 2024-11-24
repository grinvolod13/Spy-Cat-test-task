from pydantic import BaseModel, RootModel, Field
from annotated_types import Len
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
