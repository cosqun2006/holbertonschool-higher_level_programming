#!/usr/bin/python3
"""Script that prints the State object with the name passed as argument"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}{password}@localhost:3306/{db_name}"

    )
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Lousiana")

    session.add(new_state)
    session.commit()

    print(new_state.id)
    session.close()
