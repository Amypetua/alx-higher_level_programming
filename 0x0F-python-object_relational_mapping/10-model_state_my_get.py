#!/usr/bin/python3
"""
A script that lists all objects that contains a letter from a database.
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
            format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like(sys.argv[4]))
    if states.count() != 1 or not states:
        print("Not found")
    else:
        print("{}".format(states.first().id))
