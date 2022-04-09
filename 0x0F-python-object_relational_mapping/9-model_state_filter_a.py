#!/usr/bin/python3
"""
a script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy.sql import select
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()
    s = select(State)
    for i in session.query(State).filter(State.name.like('%a%')):
        print(str(i.id) + ': ' + i.name)
