#!/usr/bin/python3
"""Add new detail
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """Add new detail
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

    newState = State(name='Louisiana')
    session.add(newState)
    session.commit()

    statesFiltered = session.query(State).filter(State.name.like('Louisiana')).all()
    if statesFiltered:
        for state in statesFiltered:
            print(state.id)

    session.close()


if __name__ == "__main__":
    main()
