#!/usr/bin/python3
"""
"""

from model_state import Base, State
from sqlalchemy.sql import select
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
    Session = sessionmaker(engine)
    conn = engine.connect()
    n = State()
    updt = update(State).where(State.id == 2).values(name='New Mexico')
    result = conn.execute(updt)
