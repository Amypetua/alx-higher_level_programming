#!/usr/bin/python3
""" Class definition of a state and an instance Base = declarative_base()
"""


from sqlalchemy import Colum, Integer, String
from sqlalchemy.ext.declarative import declarative import declarative_base
from relationship_state import Base, State


class City(Base):
    """ City Class inherit from Base declarative_base()
    links to the MySQl table states Attr: id, name """

    __tablename__ = 'cities'
    id = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
