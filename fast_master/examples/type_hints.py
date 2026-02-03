from typing import List, Dict, Optional, Union, Tuple


# Variáveis com type hints
nome: str = "Felipe"
idade: int = 30
altura: float = 1.75
ativo: bool = True

# Listas e dicionários tipados
numeros: List[int] = [1, 2, 3, 4, 5]
usuario: Dict[str, str] = {"nome": "Felipe", "email": "felipe@pycode.br"}

# Função com type hints completos
def criar_usuario(
    nome: str,
    idade: int,
    email: Optional[str] = None
) -> Dict[str, Union[str, int]]:
    """Cria um dicionário com dados do usuário"""
    usuario = {
        "nome": nome,
        "idade": idade
    }
    if email:
        usuario["email"] = email
    return usuario