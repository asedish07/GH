from sqlalchemy import Column, VARCHAR, CHAR
from db.base import Base, relationship

class User(Base):
  __tablename__ = "USER"

  username = Column(VARCHAR(5), primary_key=True, unique=True, index=True, nullable=False)
  nick = Column(VARCHAR(10), default=None, nullable=True)
  hashed_password = Column(CHAR(60), nullable=False)

  writing = relationship("Writing", back_populates="user")