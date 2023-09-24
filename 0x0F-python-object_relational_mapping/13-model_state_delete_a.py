#!/usr/bin/python3
"""Update value in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """Update value in database
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
    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)
    session.commit()


if __name__ == "__main__":
    main()
