# 🗓️ API de Atividades

## 📌 Descrição

Esta API é responsável pela criação e listagem de atividades dos alunos. Ela valida a existência da turma e aluno antes de permitir a atividade e armazena os dados localmente utilizando SQLite. A aplicação foi desenvolvida com Flask e estruturada no padrão MVC, além de estar totalmente conteinerizada via Docker para facilitar a integração em um ambiente de microsserviços.

---

## 🚀 Como Executar com Docker

### Pré-requisitos

- Docker e Docker Compose instalados.
-  Ter a API de turma ativa.

### Passos

1. Clone o repositório:
   ```bash
   git clone https://github.com/Mathx8/microservice-atividade

   https://github.com/genari05/Flask.git

---
🌐 Ecossistema de Microsserviços
A **API de Atividades** faz parte de um sistema baseado em microsserviços. Atualmente, ela se integra ao seguinte serviço externo:

🔗 Serviço de Turmas
- **Descrição**: Responsável por fornecer dados das turmas existentes.

- **Integração**: A API de Atividades faz uma requisição GET para validar se a turma informada na atividade existe.

 - **Endpoint consultado:**
  ```
      GET https://flask-wbfe.onrender.com/turmas/<turma_id>

      GET https://flask-wbfe.onrender.com/alunos/<aluno_id>
```

- Se a turma for válida, a atividade é criada; caso contrário, a requisição retorna erro **400**.
- O mesmo acontece com aluno em resposta.

📬 Endpoints

POST **/atividade/**
Cria uma nova atividade.

Corpo esperado (JSON):
  ```
  {
    "id_turma": 1,
    "enunciado": "Crie um app de todo em Flask.",
  }

```
**Resposta:**
```
{
  "mensagem": "Atividade criada com sucesso"
}
```

GET **/atividade**
Lista todas as atividades:
Corpo esperado(JSON):
  ```
  {
    "enunciado": "Crie um app de todo em Flask.",
    "id": 1,
    "id_turma": 1,
    "respostas": [
      {
        "id": 1,
        "id_aluno": 2,
        "nota": 9.5,
        "resposta": "todo.py"
      }
    ]
  }
```

POST **/resposta/**
Cria uma nova resposta.

Corpo esperado (JSON):
  ```
{
  "id_atividade": 1,
  "id_aluno": 2,
  "resposta": "todo.py",
  "nota": 9.5
}
```

**Resposta:**
```
{
  "mensagem": "Resposta criada com sucesso"
}
```

GET **/resposta/<aluno_id>**
Lista todas as respostas por aluno:
Corpo esperado(JSON):
  ```
  {
    "enunciado": "Crie um app de todo em Flask.",
    "id": 1,
    "id_turma": 1,
    "respostas": [
      {
        "id": 1,
        "id_aluno": 2,
        "nota": 9.5,
        "resposta": "todo.py"
      }
    ]
  }
```

GET **/atividade/validar_turma/<turma_id>**
Verifica se uma turma existe (via serviço externo).

Resposta:
```
{
  "valida": true
}
```

GET **/resposta/validar_aluno/<aluno_id>**
Verifica se um aluno existe (via serviço externo).

Resposta:
```
{
  "valida": true
}
```

🛠️ Tecnologias Utilizadas
- Python 3.12

- Flask

- SQLite

- Docker / Docker Compose

- Padrão MVC

  🏗️ Arquitetura
A aplicação segue a **arquitetura MVC (Model-View-Controller)**.

Estrutura de Diretórios

```
.
├── client/
|   └── client.py  
├── model/
|   └── atividade.py
|   └── respostas.py
├── controller/
|   └── atividade.py
|   └── respostas.py
├── instance/      
│       └── app.db
├── docker/      
│       └── Dockerfile
│       └── docker-compose.yml
│       └── .dockerignore                 
├── app.py
├── config.py
├── requirements.txt    
└── README.md                      
```