from config import db
from flask import Flask
from controller.atividade import Atividade_Blueprint
from controller.respostas import Resposta_Blueprint

app = Flask(__name__)

app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 5002
app.config['DEBUG'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(Atividade_Blueprint, url_prefix="/atividade")
app.register_blueprint(Resposta_Blueprint, url_prefix="/resposta")

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )