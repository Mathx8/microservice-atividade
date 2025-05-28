from flask import Blueprint, jsonify, request
from model.respostas import *
from client.client import aluno_existe

Resposta_Blueprint = Blueprint('resposta', __name__)

@Resposta_Blueprint.route('/<int:id>', methods=["GET"])
def get_respostas_por_id_aluno(id):
    resposta = ListarRespostasPorAluno(id)
    if not resposta:
        return jsonify({"erro": "Respostas não encontradas"}), 404
    return jsonify([r.dici() for r in resposta])

@Resposta_Blueprint.route('/', methods=["POST"])
def create_resposta():
    dados = request.get_json()
    nova, erro = AdicionarRespostas(dados)
    if erro:
        return jsonify({"erro": erro}), 400
    return jsonify(nova.dici()), 201

@Resposta_Blueprint.route('/<int:id>', methods=["PUT"])
def update_resposta(id):
    dados = request.get_json()
    atualizada, erro = AtualizarResposta(id, dados)
    if erro:
        return jsonify({"erro": erro}), 404
    return jsonify(atualizada.dici())

@Resposta_Blueprint.route('/<int:id>', methods=["DELETE"])
def delete_resposta(id):
    sucesso, erro = DeletarResposta(id)
    if not sucesso:
        return jsonify({"erro": erro}), 404
    return jsonify({"mensagem": "Resposta deletada com sucesso"})

@Resposta_Blueprint.route('/validar_aluno/<int:aluno_id>', methods=["GET"])
def validar_aluno(aluno_id):
    existe = aluno_existe(aluno_id)
    if not existe:
        return jsonify({"valida": existe}), 404
    return jsonify({"valida": existe})