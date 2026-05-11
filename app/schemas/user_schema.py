from pydantic import BaseModel, EmailStr

# CREAR USUARIO
class UserCreate(BaseModel):
    nombre: str
    email: EmailStr
    password: str


# RESPUESTA USUARIO
class UserResponse(BaseModel):
    id: int
    nombre: str
    email: EmailStr

    class Config:
        from_attributes = True


# ACTUALIZAR USUARIO
class UserUpdate(BaseModel):
    nombre: str
    email: EmailStr
    password: str