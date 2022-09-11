#!/usr/bin/python3
""" model_state class.
    inherits from Base class.
    links to MySQL table.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """shows state of MySQL database.

    __tablename__(str): MySQL table to store States.
    id (sqlalchemy.Integer): State's id.
    name (sqlalchmey.String): States's name.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
