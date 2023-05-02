from main import app

def test_index():
    response = app.test_client().get('/')
    
    assert response.data == b'Hello, world...! It works finally again!'
    assert response.status_code == 200