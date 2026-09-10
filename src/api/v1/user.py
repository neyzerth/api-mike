from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Nombre de usuario")
    email: EmailStr = Field(..., description="Correo electrónico")
    password: str = Field(..., min_length=8, max_length=72, description="Contraseña")

class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = Field(None)
    password: Optional[str] = Field(None, min_length=8, max_length=72)
    is_active: Optional[bool] = Field(None)

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool
    created_at: datetime
