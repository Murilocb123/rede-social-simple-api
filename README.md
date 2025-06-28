Claro! Abaixo está o conteúdo atualizado do arquivo `README.md` conforme a nova rota e estrutura do projeto:

---

### 📄 `README.md`

```markdown
# 📸 API - Feed de Fotos | Rede Social

Este projeto implementa uma API RESTful com **FastAPI** para simular o **feed de postagens de uma rede social de fotos**. A aplicação faz parte do Trabalho Final da disciplina de **Cloud Computing**, com foco em práticas DevOps (CI/CD, IaC e automação de deploy).

---

## ✅ Funcionalidades

- `GET /status`: Verifica se a API está funcionando.
- `GET /feed_fotos`: Retorna as postagens de fotos mais recentes, simulando um feed realista de rede social com pelo menos 10 entradas.

---

## 🧱 Estrutura do Projeto

```

photo-api/
├── main.py                  # Arquivo principal da API
├── data/
│   └── feed\_fotos.json      # Dados simulados do feed
├── tests/
│   └── test\_api.py          # Testes unitários com Pytest
├── requirements.txt         # Dependências da aplicação
└── README.md                # Este arquivo

````

---

## 🚀 Como executar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/photo-api.git
cd photo-api
````

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv .venv
# Ative:
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a API

```bash
uvicorn main:app --reload
```

### 5. Acesse no navegador ou Postman:

* `http://localhost:8000/status`
* `http://localhost:8000/feed_fotos`

---

## 🧪 Rodando os testes

A aplicação possui testes automatizados com **pytest** para garantir o funcionamento das rotas:

```bash
pytest
```

---

## 🧾 Exemplo de retorno (`GET /feed_fotos`)

```json
[
  {
    "id_postagem": "post987",
    "url_imagem": "foto_praia_sunset.jpg",
    "usuario_nickname": "AventureiroSol",
    "descricao": "Pôr do sol incrível na praia hoje! #sunset #praia #natureza",
    "data_postagem": "2025-06-04T10:05:00Z",
    "curtidas": 152,
    "comentarios_count": 12,
    "avatar_usuario": "avatar_aventureiro.png"
  }
]
```

---

## 📘 Tecnologias utilizadas

* Python 3.11
* FastAPI
* Uvicorn
* Pytest
* HTTPX (para testes)
* 
---

### 🚀 Provisionamento da Infraestrutura com Terraform

Este projeto utiliza **Terraform** para criar uma instância EC2 na AWS que hospedará a API da rede social de fotos.

#### ✅ O que o Terraform faz:

* Cria um **Security Group** com liberação das portas 22 (SSH) e 8000 (API)
* Cria uma **instância EC2** Ubuntu 22.04 (t2.micro)
* Executa um **script de inicialização (`user_data`)** que instala `Docker` e `pip`
* Exibe o **IP público da instância** ao final

---

### ⚙️ Como executar

#### 1. Configure suas credenciais no arquivo `terraform.tfvars`:

```hcl
aws_access_key = "SUA_AWS_ACCESS_KEY"
aws_secret_key = "SUA_AWS_SECRET_KEY"
key_name       = "nome_da_sua_chave_ssh"
```

> ⚠️ **Nunca versionar este arquivo**. Mantenha ele no `.gitignore`.

---

#### 2. Execute os comandos Terraform:

```bash
cd terraform

terraform init
terraform plan -var-file="terraform.tfvars"
terraform apply -var-file="terraform.tfvars"
```

---

### 📌 Ao final

O Terraform exibirá o **endereço IP público** da instância EC2. Você usará esse IP para:

* Acessar via SSH
* Fazer o deploy da API com Ansible
* Testar a rota `GET /feed_fotos` via navegador ou Postman

---

## 👤 Autor

Trabalho desenvolvido por Murilo Costa Bittencourt e Ramon Diego Valentim
Disciplina: Cloud Computing
Professor: Ademar Perfoll Junior
Curso: Sistemas de Informação - UNIDAVI
Data de entrega: 27/06/2025

---

## 📌 Observações

Este projeto integra a primeira etapa do fluxo DevOps simulado e será utilizado nas próximas etapas com CI, Terraform e Ansible.

```
