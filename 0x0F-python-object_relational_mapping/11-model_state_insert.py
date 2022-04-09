#!/usr/bin/python3
"""
 a script that adds the State object
 “Louisiana” to the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy.sql import select
from sqlalchemy import (create_engine), update
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
    Session = sessionmaker(engine)
    ln = State()
    ln.name = "Louisiana"
    with Session.begin() as session:
        session.add(ln)
        session.commit()

    result = session.query(State).filter(State.name.like('%Louisiana%'))
    for i in result:
        print(i.id)
