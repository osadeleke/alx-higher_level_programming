#!/usr/bin/python3
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

us = sys.argv[1]
pa = sys.argv[2]
db = sys.argv[3]

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(us, pa, db),
            pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State)
    i = 1
    for state in states:
        print('{}: {}'.format(i, state.name))
        i += 1
