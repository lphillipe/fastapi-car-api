from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Modelo base
class PessoaBase(BaseModel):
    nome: str
    email: EmailStr
    telefone: Optional[str] = None

# Modelo para criação (sem ID)
class PessoaCreate(PessoaBase):
    senha: str

# Modelo completo (com ID e timestamps)
class Pessoa(PessoaBase):
    id: int
    criado_em: datetime
    atualizado_em: Optional[datetime] = None

# Modelo para resposta (sem senha)
class PessoaResponse(PessoaBase):
    id: int
    criado_em: datetime

