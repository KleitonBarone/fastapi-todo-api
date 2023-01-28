from sqlalchemy import Boolean, Column, Integer, String
from db import Base

class Todo(Base):
	__tablename__ = "todos"
	id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
	name = Column(String(255), index=True, nullable=False)
	isdone = Column(Boolean, index=True, nullable=False)
