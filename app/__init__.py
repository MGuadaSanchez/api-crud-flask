from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # Creamos la app Flask

# Configuramos la base de datos (archivo SQLite llamado database.db)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app) # Creamos instancia de SQLAlchemy vinculada a la app

from app import routes # importa las rutas para que se registren