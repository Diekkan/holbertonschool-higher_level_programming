#!/usr/bin/python3
"""
"""

from model_state import Base, State
from model_city import City
from sqlalchemy.sql import select
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
    Session = sessionmaker(engine)
    with Session.begin() as session:
        result = session.query(State, City).filter(City.state_id==State.id).all()
        for c, i in result:
            print("{}: ({}) {}".format(c.name, i.id, i.name))

