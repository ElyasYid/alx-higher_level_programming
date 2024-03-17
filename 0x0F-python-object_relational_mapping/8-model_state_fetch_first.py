#!/usr/bin/python3
"""
Prints first State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    db_engi = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                            format(sys.argv[1], sys.argv[2], sys.argv[3]),
                            pool_pre_ping=True)
    Episode = sessionmaker(bind=db_engi)
    episode = Episode()

    place = episode.query(State).order_by(State.id).first()

    print("Nothing" if not place else "{}: {}".format(place.id, place.name))
