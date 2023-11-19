#!/usr/bin/python3
"""Contains the class definition of a state and an instance 
Base = declarative_base()"""

from sqlalchemy import Column, Integer, String
from sqlalchemy import Foreignkey
from sqlalchemy.ext.declarative import declaractive_base
from model_state import Base

class City(Base):
    """City Class inherit from Base declarative_base() links to the MySQL
    table states Attr: id, name"""

    __tablename__ = 'cities'
    id = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    name = Colum(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('State.id'), nullable=False
