from . import db
from flask import jsonify, request, Blueprint
from .models import User

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return jsonify({
        'message': 'Welcome to the API',
        'routes': [
            '/users',
            '/users/<id>'
        ]
    })


@routes.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@routes.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(nombre=data['nombre'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

@routes.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())

@routes.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.nombre = data['nombre']
    user.email = data['email']
    db.session.commit()
    return jsonify(user.to_dict())

@routes.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return '', 204


