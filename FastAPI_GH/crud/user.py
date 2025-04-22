from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserRead

def create_user(db: Session, user: dict):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user