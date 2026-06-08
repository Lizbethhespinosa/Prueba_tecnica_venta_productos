from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserUpdate
from app.utils.security import hash_password
from persistence_kit.repository_factory.factory.repository_factory import (
    get_repo
)

from app.entities.user_entity import UserEntity

# CREAR
async def create_user(user: UserCreate):

    repo = get_repo("user")

    users = await repo.list()

    existing_user = next(
        (u for u in users if u.email == user.email),
        None
    )

    if existing_user:
        return {
            "error": "El email ya está registrado"
        }

    next_id = max(
        [u.id for u in users],
        default=0
    ) + 1

    new_user = UserEntity(
        id=next_id,
        nombre=user.nombre,
        email=user.email,
        password=hash_password(user.password)
    )

    await repo.add(new_user)

    return new_user

# OBTENER TODOS
async def get_users():

    repo = get_repo("user")

    return await repo.list()


# OBTENER POR ID
async def get_user_by_id(user_id: int):

    repo = get_repo("user")

    return await repo.get(user_id)


# ACTUALIZAR
async def update_user(
    user_id: int,
    user_data: UserUpdate
):

    repo = get_repo("user")

    user = await repo.get(user_id)

    if not user:
        return None

    user.nombre = user_data.nombre
    user.email = user_data.email
    user.password = user_data.password

    await repo.update(user)

    return user

# ELIMINAR
async def delete_user(
    user_id: int
):

    repo = get_repo("user")

    user = await repo.get(user_id)

    if not user:
        return None

    await repo.delete(user_id)

    return user