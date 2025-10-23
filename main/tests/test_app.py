from app import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_health():
    response = app.test_client().get('/health')
    assert b"OK" in response.data

def test_data_post():
    response = app.test_client().post('/data', json={"name": "Hanzla"})
    assert response.status_code == 201
    assert b"Data received successfully" in response.data
