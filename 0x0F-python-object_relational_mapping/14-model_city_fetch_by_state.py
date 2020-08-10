#!/usr/bin/python3
"""Lists all City objects"""
from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
         argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State).filter(City.id == State.id)\
            .order_by(City.id).all():
        print("{}: ({}) {}".format(state.id, city.id, city.name))

    session.close()
