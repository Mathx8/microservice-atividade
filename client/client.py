import requests

SERVICE_URL = "https://flask-wbfe.onrender.com"

def turma_existe(turma_id):
    try:
        resp = requests.get(f"{SERVICE_URL}/turmas/{turma_id}")
        return resp.status_code == 200
    except requests.RequestException as e:
        print(f"Erro ao conectar com serviço de turmas: {e}")
        return False
    
def aluno_existe(aluno_id):
    try:
        resp = requests.get(f"{SERVICE_URL}/alunos/{aluno_id}")
        return resp.status_code == 200
    except requests.RequestException as e:
        print(f"Erro ao conectar com serviço de turmas: {e}")
        return False