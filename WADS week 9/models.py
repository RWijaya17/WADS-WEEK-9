from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy.dialects.postgresql import UUID

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashedpassword = Column(String)
    profileURL = Column(String)

    todos = relationship("TodoItem", back_populates="owner")

class TodoItem(Base):
    __tablename__ = "todos"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    task = Column(String, index=True)
    completed = Column(Boolean, default=False)