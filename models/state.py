#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='delete', backref='state')
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            city_list= []
            for city in models.storage.all(city).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
