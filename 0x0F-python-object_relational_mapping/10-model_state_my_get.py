#!/usr/bin/python3
"""
 a script that prints the State object with
 the name passed as argument from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy.sql import select
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
    session = Session()
    s = select(State)
    lol = session.query(State).filter(State.name.like(argv[4])).first()
    if lol:
        print(lol.id)
    else:
        print('Not found')
    session.close()
