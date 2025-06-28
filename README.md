# 📸 API - Feed de Fotos | Rede Social

Este projeto implementa uma API RESTful com **FastAPI** para simular o **feed de postagens de uma rede social de fotos**. A aplicação faz parte do Trabalho Final da disciplina de **Cloud Computing**, com foco em práticas DevOps como CI/CD, Infraestrutura como Código (IaC) e automação de deploy.

---

## ✅ Funcionalidades

- `GET /status`: Verifica se a API está funcionando.
- `GET /feed_fotos`: Retorna as postagens de fotos mais recentes, simulando um feed com pelo menos 10 registros realistas.

---

## 🧱 Estrutura do Projeto

```
photo-api/
├── main.py                  # Arquivo principal da API
├── data/
│   └── feed_fotos.json      # Dados simulados do feed
├── tests/
│   └── test_api.py          # Testes unitários com Pytest
├── requirements.txt         # Dependências da aplicação
└── README.md                # Este arquivo
```

---

## 🚀 Execução local da API

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/photo-api.git
cd photo-api
```

### 2. (Opcional) Crie um ambiente virtual

```bash
python -m venv .venv
# Ative:
.venv/Scripts/activate      # Windows
source .venv/bin/activate  # Linux/macOS
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a API localmente

```bash
uvicorn main:app --reload
```

### 5. Teste no navegador ou Postman:

- `http://localhost:8000/status`
- `http://localhost:8000/feed_fotos`

---

## 🧪 Testes automatizados

A aplicação possui testes com **pytest** para garantir o funcionamento das rotas:

```bash
python -m pytest -v
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

## ☁️ Provisionamento com Terraform

Utilizamos **Terraform** para criar a infraestrutura na AWS, automatizando a criação de uma instância EC2 com ambiente pronto para execução da API.

### O Terraform realiza:

- Criação de um **Security Group** com liberação das portas 22 (SSH) e 8000 (API)
- Provisionamento de uma instância **EC2 Ubuntu 22.04 (t2.micro)**
- Execução de script de inicialização (`user_data`) que instala Docker e dependências
- Exibição do **IP público da instância**

### Como executar

1. Configure o arquivo `terraform.tfvars`:

```hcl
aws_access_key = "SUA_AWS_ACCESS_KEY"
aws_secret_key = "SUA_AWS_SECRET_KEY"
key_name       = "nome_da_sua_chave_ssh"
```

> ⚠️ Este arquivo deve estar no `.gitignore`. Nunca o versionar.

2. Execute os comandos:

```bash
cd terraform
terraform init
terraform plan -var-file="terraform.tfvars"
terraform apply -var-file="terraform.tfvars"
```

Ao final, o IP público da EC2 será exibido no terminal.

---

## 🤖 Deploy com Ansible

Após provisionar a EC2, utilizamos **Ansible** para:

- Conectar à EC2 via SSH
- Instalar `docker.io`, `docker-compose` e `git`
- Clonar o repositório da API
- Executar `docker-compose up -d --build` para subir o container da API

### Estrutura esperada:

```
ansible/
├── playbook.yml
├── hosts.yml
└── sua-chave.pem
```

### Etapas de execução

1. Dê permissão à chave SSH:

```bash
chmod 400 sua-chave.pem
```

2. Edite `hosts.yml` com o IP da EC2:

```yaml
all:
  hosts:
    api:
      ansible_host: SEU_IP_PUBLICO
      ansible_user: ubuntu
      ansible_ssh_private_key_file: ./sua-chave.pem
```

3. Teste a conexão:

```bash
ansible -i hosts.yml all -m ping
```

4. Execute o playbook:

```bash
ansible-playbook -i hosts.yml playbook.yml
```

---

### 🌐 Acesso à API

Após o deploy, acesse:

```
http://SEU_IP_PUBLICO:8000/feed_fotos
```

---

## 📘 Tecnologias utilizadas

- Python 3.11
- FastAPI
- Uvicorn
- Pytest
- HTTPX
- Docker
- Docker Compose
- Terraform
- Ansible
- AWS EC2

---

## 👤 Autor

Trabalho desenvolvido por:

- **Murilo Costa Bittencourt**  
- **Ramon Diego Valentim**

Disciplina: *Cloud Computing*  
Professor: *Ademar Perfoll Junior*  
Curso: *Sistemas de Informação – UNIDAVI*  
Data de entrega: **27/06/2025**

---

## 📌 Observações finais

Este projeto integra todas as etapas do fluxo DevOps simulado, incluindo:

- Criação da API (Etapa 1)
- Integração Contínua com GitHub Actions (Etapa 2)
- Infraestrutura como Código com Terraform (Etapa 3)
- Provisionamento e Deploy com Ansible (Etapa 4)