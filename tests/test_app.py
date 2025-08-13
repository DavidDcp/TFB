import pytest
from app import create_app, db
from app.models import Data

@pytest.fixture
def app():
    app = create_app("testing")
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Bienvenido" in response.json["message"]

def test_insert_data(client):
    response = client.post("/data", json={"name": "TestData"})
    assert response.status_code == 201
    assert response.json["message"] == "Data inserted successfully"

    # Insert duplicate
    response2 = client.post("/data", json={"name": "TestData"})
    assert response2.status_code == 409

def test_get_all_data(client):
    client.post("/data", json={"name": "Data1"})
    client.post("/data", json={"name": "Data2"})
    response = client.get("/data")
    assert response.status_code == 200
    assert len(response.json) == 2

def test_delete_data(client):
    client.post("/data", json={"name": "ToDelete"})
    data_id = Data.query.filter_by(name="ToDelete").first().id
    response = client.delete(f"/data/{data_id}")
    assert response.status_code == 200
    assert response.json["message"] == "Data deleted successfully"

    # Delete non-existent
    response2 = client.delete("/data/999")
    assert response2.status_code == 404
