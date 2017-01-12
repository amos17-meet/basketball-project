from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import *


engine = create_engine('sqlite:///fizzBuzz.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()


amos=Coach(name="amos",
			email="amos.ro7@gmail.com",
			password="123",
			nickname="amosrottenberg")

team1=Team (name="1")

ido=Player(name="ido",
	player_position=1,
	three_point=40,
	two_points=50,
	one_on_one=7,
	defense=8,
	)







session.commit()
			

