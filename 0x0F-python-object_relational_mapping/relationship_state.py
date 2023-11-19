#!/usr/bin/python3
"""
The class definition of a state and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class State(Base):
    """ State Class inherit from Base = declarative_base()
    links to the MySQl table states Attr: id, name """

    __tablename__ = 'states'
    id = Column(String, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='delete', backref="state")
