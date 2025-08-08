from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # Creamos instancia de SQLAlchemy 

def create_app():
    app = Flask(__name__) # Creamos la app Flask

    # Configuramos la base de datos (archivo SQLite llamado database.db)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app) # Inicializamos la base de datos

    from .routes import routes
    app.register_blueprint(routes)

    return app


