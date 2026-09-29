# 📚 Bookstore API

> API REST para gerenciamento de uma livraria, desenvolvida com Django REST Framework.

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.1-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django%20REST%20Framework-API-A30000?logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Poetry](https://img.shields.io/badge/Poetry-Dependency%20Manager-60A5FA?logo=poetry&logoColor=white)](https://python-poetry.org/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![Render](https://img.shields.io/badge/Render-Deploy-46E3B7?logo=render&logoColor=black)](https://render.com/)

---

## 🚀 Sobre o projeto

O **Bookstore API** é uma aplicação backend desenvolvida durante a formação **Profissão: Desenvolvedor Full Stack Python v2**, da EBAC.

O projeto foi construído utilizando **Django** e **Django REST Framework**, com foco no desenvolvimento de uma API REST para gerenciamento de produtos, categorias e pedidos.

Além do desenvolvimento da API, o projeto também contempla **autenticação, testes automatizados, PostgreSQL e pipeline de CI/CD**, com deploy da aplicação em produção através do Render.

### 🌐 API em produção

**[Acessar Bookstore API](https://ebac-bookstore-api-yftk.onrender.com)**

---

## 🛠️ Tecnologias

| Tecnologia                | Utilização                    |
| ------------------------- | ----------------------------- |
| **Python**                | Linguagem principal           |
| **Django**                | Framework web                 |
| **Django REST Framework** | Construção da API REST        |
| **PostgreSQL**            | Banco de dados em produção    |
| **Poetry**                | Gerenciamento de dependências |
| **Gunicorn**              | Servidor WSGI                 |
| **Git / GitHub**          | Versionamento                 |
| **GitHub Actions**        | CI/CD                         |
| **Render**                | Deploy e hospedagem           |

---

## ✨ Funcionalidades

- 📦 Gerenciamento de produtos
- 🗂️ Gerenciamento de categorias
- 🛒 Gerenciamento de pedidos
- 🔐 Autenticação baseada em token
- 🛡️ Controle de permissões
- 🗄️ Integração com PostgreSQL
- 🧪 Testes automatizados
- 🚀 Deploy em produção
- ⚙️ Pipeline de integração e entrega contínuas

---

## 📡 Endpoints

### Produtos

```text
GET    /bookstore/v1/product/
Categorias
GET    /bookstore/v1/category/
Pedidos
GET    /bookstore/v1/orders/

O endpoint de pedidos requer autenticação.

Autenticação
POST   /api-token-auth/
⚙️ Como executar localmente
Pré-requisitos
Python 3.12+
Poetry
Git
1. Clone o repositório
git clone https://github.com/kaio-oliveira5/bookstore.git
2. Acesse o projeto
cd bookstore
3. Instale as dependências
poetry install
4. Execute as migrações
poetry run python manage.py migrate
5. Inicie o servidor
poetry run python manage.py runserver

A aplicação estará disponível em:

http://127.0.0.1:8000/
🧪 Testes

Os testes automatizados podem ser executados com:

poetry run python manage.py test
🔄 CI/CD

O projeto utiliza GitHub Actions para automatizar o processo de integração e deploy.

A cada alteração enviada para a branch main, o workflow:

┌──────────────┐
│   Git Push   │
└──────┬───────┘
       ↓
┌──────────────┐
│    GitHub    │
└──────┬───────┘
       ↓
┌────────────────────┐
│   GitHub Actions   │
├────────────────────┤
│ Install dependencies│
│ Run automated tests │
└─────────┬──────────┘
          ↓
     Tests passed
          ↓
┌────────────────────┐
│       Render       │
│      Deploy        │
└─────────┬──────────┘
          ↓
┌────────────────────┐
│    Production API  │
└────────────────────┘

Dessa forma, alterações na branch main passam pelo processo de validação antes de acionar o deploy da aplicação.

🗄️ Banco de dados

O projeto utiliza SQLite durante o desenvolvimento local e PostgreSQL no ambiente de produção.

A conexão com o banco de produção é realizada através da variável de ambiente:

DATABASE_URL
🔐 Variáveis de ambiente

As informações sensíveis da aplicação não são armazenadas diretamente no código.

Exemplo:

SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=your-database-url

⚠️ Nunca publique valores reais de SECRET_KEY ou DATABASE_URL no repositório.

📁 Estrutura do projeto
bookstore/
├── bookstore/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── order/
├── product/
│
├── .github/
│   └── workflows/
│       ├── build.yml
│       ├── github-actions-demo.yml
│       └── worflow-pr.yml
│
├── manage.py
├── pyproject.toml
├── poetry.lock
└── README.md
📚 Objetivos de aprendizado

Este projeto foi desenvolvido para colocar em prática conceitos de:

Desenvolvimento de APIs REST
Django e Django REST Framework
Autenticação e autorização
Banco de dados relacional
Testes automatizados
Gerenciamento de dependências com Poetry
Git e GitHub
GitHub Actions
Integração contínua
Deploy de aplicações Python
CI/CD
👨‍💻 Autor
Kaio Oliveira

Desenvolvedor Full Stack Python

GitHub
```
