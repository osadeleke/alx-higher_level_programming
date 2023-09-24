#!/usr/bin/python3
"""Print states with a filter in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """Print states with a filter in database
    """
    us = sys.argv[1]
    pa = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(us, pa, db),
            pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    statesFiltered = session.query(State).filter(State.name.like('%a%')).all()
    if statesFiltered:
        for state in statesFiltered:
            print('{}: {}'.format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    main()
