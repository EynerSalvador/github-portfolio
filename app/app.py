from app.katas.kata_validation import validate_post
from app.models import Post

@app.route('/create-post', methods=['POST'])
def create_post():
    title = request.form.get('title')
    content = request.form.get('content')
    
    if not validate_post(title, content):  # Usamos la Kata aquí
        return {"error": "Título inválido"}, 400
    
    new_post = Post(title=title, content=content)  # Código existente
    db.session.add(new_post)
    db.session.commit()
    
    return {"success": True}
