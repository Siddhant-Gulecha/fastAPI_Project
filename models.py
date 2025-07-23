from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from pydantic import BaseModel, EmailStr
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True)
    age = Column(Integer)

    # Optional: Add reverse relationship for easy access
    records = relationship("Record", back_populates="user")


class Record(Base):
    __tablename__ = "Records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("Users.id", ondelete="CASCADE"))
    record_data = Column(String(100))

    # ORM relationship
    user = relationship("User", back_populates="records")

