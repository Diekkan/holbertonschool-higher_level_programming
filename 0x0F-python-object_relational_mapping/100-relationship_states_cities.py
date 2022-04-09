#!/usr/bin/python3
"""
"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.sql import select
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
    Session = sessionmaker(engine)
    ln = State()
    rn = City()
    ln.name = "California"
    rn.name = "San Francisco"
    rn.state_id=ln.id
    with Session.begin() as session:
        session.add(ln)
        session.commit()
