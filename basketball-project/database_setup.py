from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func

Base = declarative_base()

class Coach(Base):
    __tablename__ = 'coach'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    nickname = Column(String)

association_table = Table('association', Base.metadata,
    Column('player_id', Integer, ForeignKey('player.id')),
    Column('team_name', Integer, ForeignKey('team.name')))


class Player(Base):
    __tablename__ = 'player'
    id = Column(Integer, primary_key=True)
    name=Column(String)
    coach_id = Column(Integer, ForeignKey("coach.id"))
    #coach_id = relationship("Coach", back_populates="id")
    player_teams=relationship("Team", secondary=association_table, back_populates="players")
    player_position= Column(Integer)
    three_point = Column(Integer)
    two_points = Column(Integer)
    one_on_one = Column(Integer)
    defense = Column(Integer)


class Team(Base):
    __tablename__ = 'team'
    id = Column (Integer, primary_key=True)
    coach_id = Column(Integer, ForeignKey("coach.id"))
    #coach_id = relationship("Coach", back_populates="id")
    name = Column(String)
    players =relationship("Player", secondary=association_table, back_populates="player_teams")


