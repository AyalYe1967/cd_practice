import pytest
# מייבאים את אובייקט ה-app האמיתי מהקובץ app.py שלך
from app import app

@pytest.fixture
def client():
    # מגדירים קליינט זמני לבדיקות של Flask
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    # בדיקה עבור דף הבית (/)
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, DevOps World!" in response.data

def test_greet_route(client):
    # בדיקה עבור הנתיב הדינמי (/hello/DevOps)
    response = client.get('/hello/DevOps')
    assert response.status_code == 200
    assert b"Hello DevOps, welcome to my Flask server!" in response.data
