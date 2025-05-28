from flask import Blueprint, jsonify
from model.atividade import *
from client.client import turma_existe

Atividade_Blueprint = Blueprint('atividade', __name__)

@Atividade_Blueprint.route('/', methods=["GET"])
def get_atividades():
    atividades = ListarAtividades()
    return jsonify([a.dici() for a in atividades])

@Atividade_Blueprint.route('/<int:id>', methods=["GET"])
def get_atividade_por_id(id):
    atividade = ListarAtividadePorId(id)
    if not atividade:
        return jsonify({"erro": "Atividade não encontrada"}), 404
    return jsonify(atividade.dici())

@Atividade_Blueprint.route('/', methods=["POST"])
def create_atividade():
    dados = request.get_json()
    nova, erro = CriarAtividade(dados)
    if erro:
        return jsonify({"erro": erro}), 400
    return jsonify(nova.dici()), 201

@Atividade_Blueprint.route('/<int:id>', methods=["PUT"])
def update_atividade(id):
    dados = request.get_json()
    atualizada, erro = AtualizarAtividade(id, dados)
    if erro:
        return jsonify({"erro": erro}), 404
    return jsonify(atualizada.dici())

@Atividade_Blueprint.route('/<int:id>', methods=["DELETE"])
def delete_atividade(id):
    sucesso, erro = DeletarAtividade(id)
    if not sucesso:
        return jsonify({"erro": erro}), 404
    return jsonify({"mensagem": "Atividade deletada com sucesso"})

@Atividade_Blueprint.route('/validar_turma/<int:turma_id>', methods=["GET"])
def validar_turma(turma_id):
    existe = turma_existe(turma_id)
    if not existe:
        return jsonify({"valida": existe}), 404
    return jsonify({"valida": existe})