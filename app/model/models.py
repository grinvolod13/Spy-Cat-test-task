from sqlalchemy.types import String
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from typing import Optional
from app.dependency import engine


class Base(DeclarativeBase):
    ...

class Cat(Base):
    __tablename__ = 'cat'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    name: Mapped[str]= mapped_column()
    years_of_experience: Mapped[float] = mapped_column(default=0)
    breed: Mapped[str]
    salary: Mapped[float]
    mission: Mapped[list['Mission']] = relationship(back_populates='cat')
    
    # without data validation yet, we assume endpoint's validation is correct.
    # we may add later ValueError in validation, and handle in fastapi
    
    


class Mission(Base):
    __tablename__ = 'mission'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    cat_id: Mapped[int] = mapped_column(ForeignKey('cat.id'), nullable=True)
    cat: Mapped[Cat|None] = relationship(back_populates='mission')
        
    targets: Mapped[list['Target']] = relationship()
    complete: Mapped[bool] = mapped_column(default=False)

class Target(Base):
    __tablename__ = 'target'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    mission_id: Mapped[int]= mapped_column(ForeignKey('mission.id'))
    name: Mapped[String] = mapped_column(String)
    country: Mapped[String] = mapped_column(String)
    notes : Mapped[String] = mapped_column(String(1024), default="")
    complete: Mapped[bool] = mapped_column(default=False)
    
Base.metadata.create_all(engine)