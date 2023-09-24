#!/usr/bin/python3
"""Print states with a filter from argument in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """Print states with a filter from argument in database
    """
    us = sys.argv[1]
    pa = sys.argv[2]
    db = sys.argv[3]
    sn = sys.argv[4]

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(us, pa, db),
            pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    statesFiltered = session.query(State).filter(State.name.like(sn)).all()
    if statesFiltered:
        for state in statesFiltered:
            print(state.id)
    else:
        print('Not found')

    session.close()


if __name__ == "__main__":
    main()
