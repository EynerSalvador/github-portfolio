from flask import Flask

app = Flask(__name__)

# Configuración de la base de datos (si usas SQLAlchemy)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Importa rutas o modelos al final para evitar dependencias circulares
from app import models
