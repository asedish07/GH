from sqlalchemy import Column, Integer, VARCHAR, DateTime, BOOLEAN, ForeignKey
from sqlalchemy.sql import func

from db.base import Base, relationship

class Writing(Base):
  __tablename__ = "WRITING"

  id = Column(Integer, primary_key=True, unique=True, index=True, nullable=False, autoincrement=True)
  title = Column(VARCHAR(100), nullable=False)
  detail = Column(VARCHAR(10000), nullable=False)
  date = Column(DateTime, default=func.now(), nullable=False, onupdate=func.now())
  edit = Column(BOOLEAN, default=False, nullable=False, onupdate=True)
  author = Column(VARCHAR(5), ForeignKey("USER.nick", ondelete="CASCADE"), nullable=False)

  user = relationship("User", back_populates="writing")
  tag = relationship("Tag", back_populates="writing")

class Tag(Base):
  __tablename__ = "TAG"

  id = Column(Integer, primary_key=True, unique=True, index=True, nullable=False, autoincrement=True)
  writing_id = Column(Integer, ForeignKey("WRITING.id", ondelete="CASCADE"), nullable=False)
  tag = Column(VARCHAR(20), nullable=False)

  writing = relationship("Writing", back_populates="tag")