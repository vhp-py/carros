# Carros — Sistema de Gestão de Estoque de Veículos

Aplicação web desenvolvida com **Django** para gerenciamento de estoque de uma loja de carros, com autenticação de usuários, CRUD completo de veículos e geração automática de descrições de venda usando **IA (API da OpenAI)**.

---

## Funcionalidades

- **Cadastro e login de usuários** — registro, autenticação e logout com sistema de sessões do Django
- **Listagem de veículos** — exibição de todos os carros cadastrados com busca por modelo
- **Cadastro de veículos** — formulário com validações customizadas (valor mínimo, ano de fabricação)
- **Detalhes do veículo** — página individual com foto, dados e descrição gerada por IA
- **Edição e exclusão** — atualização e remoção de veículos (restrito a usuários autenticados)
- **Descrição automática por IA** — ao salvar um carro sem bio, uma descrição comercial é gerada automaticamente via API da OpenAI
- **Histórico de inventário** — snapshot automático do estoque (quantidade e valor total) a cada inclusão/alteração/exclusão de veículo
- **Painel administrativo** — gerenciamento de marcas e veículos via Django Admin

---

## Tecnologias utilizadas

| Tecnologia | Uso |
|---|---|
| **Python 3.12** | Linguagem principal |
| **Django 6.1** | Framework web (MTV, ORM, auth, admin, forms) |
| **SQLite** | Banco de dados |
| **OpenAI API** | Geração de descrições de veículos com IA |
| **Pillow** | Processamento de imagens (upload de fotos) |
| **HTML/CSS** | Templates Django com estilos customizados |

---

## Estrutura do projeto

```
carros/
├── app/                    # Configurações do projeto Django
│   ├── settings.py
│   ├── urls.py
│   └── templates/          # Templates base
├── accounts/               # App de autenticação (registro, login, logout)
│   └── templates/
├── cars/                   # App principal de veículos
│   ├── models.py           # Models: Car, Brand, CarInventory
│   ├── views.py            # Views: List, Detail, Create, Update, Delete
│   ├── forms.py            # Formulário com validações customizadas
│   ├── signals.py          # Signals para IA e inventário
│   └── templates/          # Templates do app cars
├── openai_api/             # Cliente de integração com OpenAI
├── media/                  # Upload de fotos dos veículos
└── requirements.txt
```

---

## Como executar

### Pré-requisitos

- Python 3.12+
- Chave de API da OpenAI (opcional — apenas para a funcionalidade de IA)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/vitor/carros.git
cd carros

# Crie e ative um ambiente virtual
python3 -m venv .venv
source .venv/bin/activate        # Linux/macOS
# .venv\Scripts\activate         # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python3 manage.py migrate

# Crie um superusuário (para acessar o /admin)
python3 manage.py createsuperuser

# Configure a variável de ambiente (opcional, para IA)
cp .env.example .env
# Edite o .env e adicione sua chave: OPENCODE_API_KEY=sk-...

# Inicie o servidor
python3 manage.py runserver
```

Acesse em `http://127.0.0.1:8000/cars/`

---

## Rotas da aplicação

| Rota | Descrição | Acesso |
|---|---|---|
| `/register/` | Cadastro de usuário | Público |
| `/login/` | Login | Público |
| `/logout/` | Logout | Autenticado |
| `/cars/` | Lista de veículos (com busca) | Público |
| `/new_car` | Cadastrar novo veículo | Autenticado |
| `/car/<id>/` | Detalhes do veículo | Público |
| `/car/<id>/update/` | Editar veículo | Autenticado |
| `/car/<id>/delete/` | Excluir veículo | Autenticado |
| `/admin/` | Painel administrativo | Staff |

---

## Destaques técnicos

- **Class-Based Views (CBVs)** — uso de `ListView`, `CreateView`, `DetailView`, `UpdateView` e `DeleteView` para um CRUD limpo e reutilizável
- **Django Signals** — `pre_save` para gerar bio via IA automaticamente, `post_save`/`post_delete` para registrar snapshots do inventário
- **Validações customizadas em Forms** — regras de negócio no `clean()` (valor mínimo de R$ 20.000, ano de fabricação a partir de 1974)
- **Integração com IA** — cliente OpenAI encapsulado em módulo separado, com prompt em português para descrições comerciais
- **Controle de acesso** — rotas protegidas com `@login_required` via `method_decorator`

---

## Licença

Este projeto foi desenvolvido para fins de estudo e portfólio.
