#!/usr/bin/python3
"""
a script that prints the first State object
from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy.sql import select
from sqlalchemy import (create_engine)
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    conn = engine.connect()
    s = select(State)
    result = conn.execute(s)
    result = result.fetchone()
    if (not result):
        print('Nothing')
    else:
        result = str(result[0]) + ': ' + str(result[1])
        print(result)
