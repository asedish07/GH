from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """Hash a password using bcrypt."""
    return bcrypt_context.hash(password)