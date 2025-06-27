### 📄 `README.md`

```markdown
# 📸 API de Rede Social de Fotos

Esta é uma API RESTful simples desenvolvida com **FastAPI** em Python, simulando uma rede social onde usuários compartilham fotos. Esta aplicação faz parte do projeto da disciplina de **Cloud Computing**, com foco em implantação de API e automação DevOps.

## ✅ Funcionalidades

- `GET /status` – Verifica se a API está funcionando.
- `GET /fotos` – Retorna uma lista de 10 registros realistas de fotos postadas por usuários.

---

## 🧱 Estrutura do Projeto

```

photo-api/
├── main.py                # Arquivo principal da API
├── data/
│   └── fotos.json         # Arquivo com os dados simulados
├── tests/
│   └── test\_api.py        # Testes unitários com Pytest
├── requirements.txt       # Lista de dependências do projeto
└── README.md              # Documentação do projeto

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
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Inicie a API

```bash
uvicorn main:app --reload
```

Acesse:

* `http://localhost:8000/status`
* `http://localhost:8000/fotos`

---

## 🧪 Rodando os testes unitários

Os testes foram criados com **Pytest** e podem ser executados com:

```bash
python -m pytest -v   
```

---

## 📦 Requisitos

* Python 3.9+
* FastAPI
* Uvicorn
* Pytest

---

## 📝 Autor

Trabalho acadêmico desenvolvido por Murilo Costa Bittencourt e Ramon Diego Valentim para a disciplina de Cloud Computing do curso de Sistemas de Informação – UNIDAVI.

Professor: Ademar Perfoll Junior

