import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(60), index= True, unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(60), nullable=False)
    subscription_date = Column(DateTime, nullable=False)
    first_name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    birthdate = Column(Date)
    favorites = relationship("Favorites", back_populates="user")

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), unique=True, nullable=False)
    user = relationship("User", back_populates="favorites")
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=False)
    species_id = Column(Integer, ForeignKey('species.id'), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=False)
    character = relationship("Characters", back_populates="favorites")
    species = relationship("Species", back_populates="favorites")
    vehicle = relationship("Vehicles", back_populates="favorites")
    planet = relationship("Planets", back_populates="favorites")

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), index= True, nullable=False)
    birth_year = Column(Integer)
    homeworld = Column(String(250), ForeignKey('planets.id'))
    gender = Column(String(250))
    eye_color = Column(String(250))
    hair_color = Column(String(250))
    height = Column(Integer)
    mass = Column(Integer)
    skin_color = Column(String(250))
    favorites = relationship("Favorites", back_populates="character")

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), index= True, nullable=False)
    climate = Column(String(250), index= True)
    population = Column(Integer)
    terrain = Column(String(250))
    diameter = Column(Integer)
    surface_water = Column(Integer)
    gravity = Column(String(250))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    favorites = relationship("Favorites", back_populates="planet")

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), index= True, nullable=False)
    classification = Column(String(250), index= True)
    designation = Column(String(250))
    language = Column(String(250))
    average_height = Column(Integer)
    average_lifespan = Column(Integer)
    eye_colors = Column(String(250))
    hair_colors = Column(String(250))
    skin_colors = Column(String(250))
    favorites = relationship("Favorites", back_populates="species")

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), index= True, nullable=False)
    model = Column(String(250), index= True)
    vehicle_class = Column(String(250))
    consumables = Column(String(250))
    length = Column(Integer)
    max_atmostphering_speed = Column(Integer)
    cargo_capacity = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    manufacturer = Column(String(250))
    favorites = relationship("Favorites", back_populates="vehicle")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
