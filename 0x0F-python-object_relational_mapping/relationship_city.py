#!/usr/bin/python3
""" model_city class.
    inherits from Base class.
    links to MySQL table.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """shows city for MySQL database.

    __tablename__(str): MySQL table to store States.
    id (sqlalchemy.Integer): State's id.
    name (sqlalchmey.String): States's name.
    state_id (sqlalchemy.Integer): Cities states id.
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
