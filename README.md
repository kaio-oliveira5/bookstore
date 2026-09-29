# 📚 Bookstore API

API REST desenvolvida com **Django REST Framework**, criada como projeto prático durante o curso **Profissão: Desenvolvedor Full Stack Python v2 — EBAC**.

O projeto implementa uma API para gerenciamento de produtos, categorias e pedidos, utilizando PostgreSQL em produção, autenticação, testes automatizados e pipeline de CI/CD com GitHub Actions e Render.

## 🌐 Projeto em produção

### 🏠 Página inicial

[Bookstore API](https://ebac-bookstore-api-yftk.onrender.com/)

### 🔗 API Endpoints

- [Products](https://ebac-bookstore-api-yftk.onrender.com/bookstore/v1/product/)
- [Categories](https://ebac-bookstore-api-yftk.onrender.com/bookstore/v1/category/)
- [Orders](https://ebac-bookstore-api-yftk.onrender.com/bookstore/v1/orders/)
- [Admin](https://ebac-bookstore-api-yftk.onrender.com/admin/login/)

---

## 🚀 Tecnologias

- Python
- Django
- Django REST Framework
- PostgreSQL
- SQLite
- Poetry
- Git
- GitHub
- GitHub Actions
- Render
- Gunicorn
- WhiteNoise
- Docker
- Django Debug Toolbar
- REST API
- Token Authentication

---

## 📌 Funcionalidades

- 🏠 Página inicial da aplicação
- 📦 Gerenciamento de produtos
- 🏷️ Gerenciamento de categorias
- 🛒 Gerenciamento de pedidos
- 🔐 Autenticação utilizando Token Authentication
- 👤 Painel administrativo do Django
- 📄 Paginação dos resultados da API
- 🗄️ Integração com PostgreSQL
- 🧪 Testes automatizados com Django
- 🎨 Arquivos estáticos configurados para produção
- ⚡ Deploy automatizado utilizando GitHub Actions
- ☁️ Aplicação hospedada no Render

---

## 🔗 Endpoints

### Products

```text
GET /bookstore/v1/product/

Endpoint responsável pelos produtos da aplicação.

Categories
GET /bookstore/v1/category/

Endpoint responsável pelas categorias dos produtos.

Orders
GET /bookstore/v1/orders/

Endpoint responsável pelos pedidos.

Esse endpoint requer autenticação.

Authentication
POST /api-token-auth/

Endpoint utilizado para obtenção do token de autenticação.

Admin
/admin/

Painel administrativo do Django.

🏠 Página inicial

A aplicação possui uma página inicial desenvolvida com HTML e CSS, oferecendo acesso rápido aos principais recursos da API.

A página apresenta:

Products
Categories
Orders
Admin

O CSS é carregado através do sistema de arquivos estáticos do Django e servido em produção utilizando WhiteNoise.

🛠️ Como executar o projeto localmente
1. Clonar o repositório
git clone https://github.com/kaio-oliveira5/bookstore.git

Entrar no diretório:

cd bookstore
2. Instalar as dependências

O projeto utiliza Poetry.

poetry install
3. Configurar as variáveis de ambiente

Defina as variáveis necessárias:

SECRET_KEY
DEBUG
DATABASE_URL
DJANGO_ALLOWED_HOSTS

Para desenvolvimento local, por exemplo:

export SECRET_KEY=dev-secret-key
export DEBUG=1
4. Executar as migrações
poetry run python manage.py migrate
5. Criar um superusuário
poetry run python manage.py createsuperuser
6. Executar o servidor
poetry run python manage.py runserver

A aplicação estará disponível em:

http://127.0.0.1:8000/
🧪 Testes

Os testes automatizados podem ser executados utilizando:

poetry run python manage.py test

O projeto também possui testes executados automaticamente através do GitHub Actions.

🔄 Integração Contínua e Deploy

O projeto utiliza GitHub Actions para automatizar o processo de validação e deploy.

O fluxo principal é:

Git Push
   ↓
GitHub Actions
   ↓
Instalação das dependências
   ↓
Execução dos testes
   ↓
Deploy Hook
   ↓
Render
   ↓
Aplicação em produção

O workflow principal executa os testes antes de iniciar o deploy.

O deploy para o Render é acionado através de um Deploy Hook, evitando a necessidade de realizar o deploy manualmente após cada alteração aprovada pelo pipeline.

☁️ Deploy

A aplicação está hospedada no Render.

Ambiente de produção
Web Service: ebac-bookstore-api
Banco de dados: PostgreSQL
Servidor WSGI: Gunicorn
Arquivos estáticos: WhiteNoise
Deploy: GitHub Actions + Render Deploy Hook
Build

O processo de build executa:

poetry install && poetry run python manage.py collectstatic --noinput
Start

O serviço é iniciado utilizando:

python manage.py migrate && gunicorn bookstore.wsgi
🗄️ Banco de dados

O projeto utiliza:

SQLite para desenvolvimento local
PostgreSQL no ambiente de produção

A conexão com o banco de produção é realizada através da variável de ambiente:

DATABASE_URL
📂 Estrutura do projeto
bookstore/
│
├── bookstore/
│   ├── templates/
│   │   └── home.html
│   │
│   ├── static/
│   │   └── css/
│   │       └── home.css
│   │
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── order/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── product/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── .github/
│   └── workflows/
│       ├── build.yml
│       ├── github-actions-demo.yml
│       └── worflow-pr.yml
│
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── poetry.lock
├── manage.py
└── README.md
🔐 Variáveis de ambiente

As informações sensíveis não são armazenadas diretamente no código.

Principais variáveis utilizadas:

SECRET_KEY
DEBUG
DATABASE_URL
DJANGO_ALLOWED_HOSTS

As variáveis de produção são configuradas no ambiente do Render.

📚 Objetivos de aprendizagem

Este projeto foi desenvolvido como parte do processo de aprendizado em desenvolvimento Full Stack Python, colocando em prática conceitos como:

Desenvolvimento de APIs REST
Django REST Framework
Serializers
ViewSets
Autenticação
Paginação
Banco de dados relacional
PostgreSQL
Testes automatizados
Poetry
Git e GitHub
Docker
GitHub Actions
Integração Contínua
Deploy em ambiente cloud
Configuração de arquivos estáticos
Gunicorn
WhiteNoise
Variáveis de ambiente
👨‍💻 Autor

Kaio Oliveira

Desenvolvedor Full Stack Python em formação.

GitHub: kaio-oliveira5
📄 Licença

Este projeto foi desenvolvido para fins educacionais e de portfólio.
```
