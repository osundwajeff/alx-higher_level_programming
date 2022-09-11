#!/usr/bin/python3
""" model_state class.
    inherits from Base class.
    links to MySQL table.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """shows state of MySQL database.

    __tablename__(str): MySQL table to store States.
    id (sqlalchemy.Integer): State's id.
    name (sqlalchmey.String): States's name.
    cities (sqlalchemy.orm.relationship): State-City relationship.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
