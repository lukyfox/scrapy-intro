from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class Estate(Base):
    __tablename__ = "estate"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)


class Image(Base):
    __tablename__ = "image"
    id = Column(Integer, primary_key=True)
    link = Column(String, nullable=False)
    estate_id = Column(Integer, ForeignKey("estate.id"))
    