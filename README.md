# FastAPI Car API

Uma API REST completa e moderna para gerenciamento de veículos, construída com **FastAPI** e **SQLAlchemy**. Oferece operações CRUD para carros, marcas e usuários, com autenticação JWT, validação de dados e testes automatizados.

## 🚀 Funcionalidades

- **Autenticação e Autorização**: Sistema de autenticação baseado em JWT (JSON Web Tokens)
- **Gestão de Usuários**: Cadastro, edição e exclusão de contas de usuário
- **Gestão de Marcas**: Cadastro e gerenciamento de marcas de veículos
- **Gestão de Carros**: Cadastro e gerenciamento de veículos com informações detalhadas
- **Busca e Filtragem**: Recursos avançados de busca e filtragem para encontrar veículos rapidamente
- **Validação de Dados**: Validações rigorosas usando Pydantic para garantir integridade dos dados
- **Segurança**: Hash de senhas com Argon2 e controle de acesso baseado em propriedade
- **Testes Automatizados**: Suite de testes com Pytest para garantir qualidade e estabilidade
- **Documentação Automática**: Swagger UI e ReDoc integrados

## 🛠️ Tecnologias

| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| Python | 3.13+ | Linguagem principal |
| FastAPI | 0.128.x | Framework web |
| SQLAlchemy | 2.0.46+ | ORM |
| Pydantic | 2.12.x | Validação de dados |
| PyJWT | 2.11.x | Autenticação JWT |
| Alembic | 1.18.x | Migrações de banco de dados |
| pwdlib[argon2] | 0.3.x | Hash de senhas |
| Pytest | 8.x | Framework de testes |
| SQLite | - | Banco de dados (padrão) |
| PostgreSQL | - | Banco de dados (produção) |

## 📋 Pré-requisitos

- Python 3.13 ou superior
- Poetry (gerenciador de dependências)

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd fastapi-car-api
```

### 2. Instale as dependências

```bash
poetry install
```

### 3. Configure as variáveis de ambiente

```bash
cp .env.example .env
```

Gere uma chave secreta JWT:

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

Adicione o valor gerado no arquivo `.env` como `JWT_SECRET_KEY`.

### 4. Execute as migrações do banco de dados

```bash
poetry run alembic upgrade head
```

## 🏃 Executando a Aplicação

### Modo de Desenvolvimento (com recarregamento automático)

```bash
poetry run fastapi dev car_api/app.py
```

Ou usando taskipy:

```bash
poetry run task run
```

### Modo de Produção

```bash
poetry run uvicorn car_api.app:app --host 0.0.0.0 --port 8000
```

A API estará disponível em `http://localhost:8000`.

## 📚 Documentação da API

Após iniciar a aplicação, acesse:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health_check

## 🔌 Endpoints Principais

### Autenticação
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/api/v1/auth/token` | Gerar token de acesso |
| POST | `/api/v1/auth/refresh_token` | Atualizar token de acesso |

### Usuários
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/api/v1/users/` | Criar novo usuário |
| GET | `/api/v1/users/` | Listar usuários |
| GET | `/api/v1/users/{user_id}` | Buscar usuário por ID |
| PUT | `/api/v1/users/{user_id}` | Atualizar usuário |
| DELETE | `/api/v1/users/{user_id}` | Deletar usuário |

### Marcas
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/api/v1/brands/` | Criar nova marca |
| GET | `/api/v1/brands/` | Listar marcas |
| GET | `/api/v1/brands/{brand_id}` | Buscar marca por ID |
| PUT | `/api/v1/brands/{brand_id}` | Atualizar marca |
| DELETE | `/api/v1/brands/{brand_id}` | Deletar marca |

### Carros
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/api/v1/cars/` | Criar novo carro |
| GET | `/api/v1/cars/` | Listar carros do proprietário |
| GET | `/api/v1/cars/{car_id}` | Buscar carro por ID |
| PUT | `/api/v1/cars/{car_id}` | Atualizar carro |
| DELETE | `/api/v1/cars/{car_id}` | Deletar carro |

## 🧪 Testes

Execute a suite de testes:

```bash
poetry run pytest
```

Com cobertura de código:

```bash
poetry run task test
```

O relatório HTML de cobertura será gerado em `htmlcov/index.html`.

## 📁 Estrutura do Projeto

```
fastapi-car-api/
├── car_api/
│   ├── __init__.py
│   ├── app.py              # Ponto de entrada da aplicação
│   ├── core/
│   │   ├── database.py     # Configuração do banco de dados
│   │   ├── security.py     # Autenticação e segurança
│   │   └── settings.py     # Configurações da aplicação
│   ├── models/
│   │   ├── cars.py         # Modelos Car e Brand
│   │   └── users.py        # Modelo User
│   ├── routers/
│   │   ├── auth.py         # Endpoints de autenticação
│   │   ├── brands.py       # Endpoints de marcas
│   │   ├── cars.py         # Endpoints de carros
│   │   └── users.py        # Endpoints de usuários
│   └── schemas/
│       ├── auth.py         # Schemas de autenticação
│       ├── brands.py       # Schemas de marcas
│       ├── cars.py         # Schemas de carros
│       └── users.py        # Schemas de usuários
├── tests/
│   ├── conftest.py         # Fixtures e configuração de testes
│   ├── test_auth.py
│   ├── test_brands.py
│   ├── test_cars.py
│   ├── test_db.py
│   └── test_users.py
├── migrations/              # Scripts de migração do Alembic
├── docs/                    # Documentação do projeto
├── pyproject.toml           # Configuração do projeto
├── alembic.ini              # Configuração do Alembic
└── README.md
```

## 🔧 Comandos Úteis

```bash
# Verificar linting
poetry run task lint

# Formatar código
poetry run task format

# Executar testes
poetry run task test

# Visualizar documentação
poetry run task docs
```

## 📖 Documentação Completa

A documentação completa do projeto está disponível em `docs/` e pode ser visualizada localmente com:

```bash
poetry run task docs
```

A documentação estará disponível em http://127.0.0.1:8001.

## 🤝 Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

Consulte [docs/contribution.md](docs/contribution.md) para mais detalhes.

## 📝 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Suporte

Para dúvidas, problemas ou sugestões:

- Abra uma [issue](https://github.com/lphillipe/fastapi-car-api/issues)
- Consulte a [documentação](docs/)
- Verifique os [endpoints da API](docs/api_endpoints.md)

---

<div align="center">


[Documentação](docs/) • [API Endpoints](docs/api_endpoints.md) • [Contribuição](docs/contribution.md)

</div>
