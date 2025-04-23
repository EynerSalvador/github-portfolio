from flask import Flask
from app.models import db, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db/database.db'
db.init_app(app)

# Crear tablas antes de las pruebas
@app.before_first_request
def create_tables():
    db.create_all()

# Ruta de ejemplo
@app.route('/posts')
def get_posts():
    posts = Post.query.all()
    return {"posts": [post.to_dict() for post in posts]}
