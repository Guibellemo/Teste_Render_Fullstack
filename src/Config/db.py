from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def init_db(app):
    uri = os.getenv("DATABASE_URL", "postgresql://usuario:senha@db:5432/mamutedb")

    # Corrige prefixo para compatibilidade com Render e SQLAlchemy
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    app.config["SQLALCHEMY_DATABASE_URI"] = uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Cria tabelas, mas sem travar o app se o banco ainda não estiver pronto
    with app.app_context():
        try:
            db.create_all()
        except Exception as e:
            print(f"Banco ainda não disponível: {e}")
