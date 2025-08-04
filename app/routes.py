from app import app, db
from flask import jsonify, request
from app.models import User


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(nombre=data['nombre'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

@app.route('/users/<int:id>', methods=['GET'])
def update_user(id):
    user = User.query.get(id)
    data = request.get_json()
    user.nombre = data['nombre']
    user.email = data['email']
    db.session.commit()
    return jsonify(user.to_dict())

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return '', 204


