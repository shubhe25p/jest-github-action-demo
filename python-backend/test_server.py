from server import app

def test_index_route():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello, World!'

def test_add():
    response = app.test_client().post(
        '/add',
        headers={'Content-Type': 'application/json'},
        data='{"title": "test", "description": "test"}'
    )
    
    assert response.data.decode('utf-8') == 'Added a new todo!'
