from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash_password(password: str):
    """Transforma a senha em uma hash segura"""

    # Use: password=hash_password(user_data.password)

    return pwd_context.hash(password)