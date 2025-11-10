from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def init_db(app):
    # Pega a URL do banco do Render
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        # Fallback para desenvolvimento local
        database_url = "postgresql://postgres:postgres@db:5432/meubanco"

    # Corrige URLs antigas que começam com postgres://
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)

    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    return db
