from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserUpdate
from app.utils.security import hash_password

# CREAR
def create_user(db: Session, user: UserCreate):

    # VALIDAR EMAIL DUPLICADO
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:

        return {
            "error": "El email ya está registrado"
        }

    new_user = User(
        nombre=user.nombre,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# OBTENER TODOS
def get_users(db: Session):

    return db.query(User).all()


# OBTENER POR ID
def get_user_by_id(db: Session, user_id: int):

    return db.query(User).filter(User.id == user_id).first()


# ACTUALIZAR
def update_user(
    db: Session,
    user_id: int,
    user_data: UserUpdate
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        return None

    user.nombre = user_data.nombre
    user.email = user_data.email
    user.password = user_data.password

    db.commit()
    db.refresh(user)

    return user


# ELIMINAR
def delete_user(db: Session, user_id: int):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        return None

    db.delete(user)
    db.commit()

    return user