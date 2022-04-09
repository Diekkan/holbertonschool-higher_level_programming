#!/usr/bin/python3
"""
10-
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
    Session = sessionmaker(engine)
    session = Session()
    s = select(State)
    result = session.query(State).filter(State.name.like('%' + argv[4] + '%'))
    flag = 0
    for i in result:
        print(str(i.id))
        flag = 1
    if flag == 0:
        print('Not found')