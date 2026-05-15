#!/usr/bin/python3
"""Script that changes the name of a State object from the database."""
import sys
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State, City).join(City).order_by(City_id).all()
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
