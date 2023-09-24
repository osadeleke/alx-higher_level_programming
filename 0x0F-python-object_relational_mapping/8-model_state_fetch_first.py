#!/usr/bin/python3
"""Print one state in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """Print one state in database
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
    firstState = session.query(State).first()
    if firstState:
        print('1: {}'.format(firstState.name))
    else:
        print('Nothing')

    session.close()


if __name__ == "__main__":
    main()
