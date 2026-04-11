#!/usr/bin/python3
"""Script that prints the State object with the name passed as argument"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    username, password, db_name, state_name = \
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    )

    with Session(engine) as session:
        state = session.query(State)\
            .filter(State.name == state_name)\
            .first()
        print(state.id if state else "Not found")
