import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

    with app.app_context():
        db.drop_all()

def test_get_users_empty(client):
    rv = client.get('/users')
    assert rv.status_code == 200
    assert rv.json == []

def test_add_user(client):
    rv = client.post('/users', json={
        'nombre': 'test',
        'email': 'test@example.com'
    })
    assert rv.status_code == 201
    assert rv.json['nombre'] == 'test'

    rv = client.get('/users')
    assert rv.status_code == 200
    assert len(rv.json) == 1

def test_update_user(client):
    rv = client.post('/users', json={
        'nombre': 'test',
        'email': 'test@example.com'
    })
    user_id = rv.json['id']

    rv = client.put(f'/users/{user_id}', json={
        'nombre': 'updated',
        'email': 'updated@example.com'
    })
    assert rv.status_code == 200
    assert rv.json['nombre'] == 'updated'

def test_delete_user(client):
    rv = client.post('/users', json={
        'nombre': 'test',
        'email': 'test@example.com'
    })
    user_id = rv.json['id']

    rv = client.delete(f'/users/{user_id}')
    assert rv.status_code == 204

    rv = client.get(f'/users/{user_id}')
    assert rv.status_code == 404
