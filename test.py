import pytest
from app import create_app, db

@pytest.fixture
def client():
    # Configura la app en modo testing
    app = create_app("development")
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })

    # Crea la BD, levanta el test client y destruye al acabar
    with app.app_context():
        db.create_all()
        with app.test_client() as client:
            yield client
        db.session.remove()
        db.drop_all()


def test_insert_data(client):
    response = client.post("/data", json={"name": "Test"})
    assert response.status_code == 200


def test_get_all_data(client):
    client.post("/data", json={"name": "User1"})
    client.post("/data", json={"name": "User2"})
    response = client.get("/data")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 2


def test_delete_data(client):
    client.post("/data", json={"name": "DeleteMe"})
    data = client.get("/data").get_json()
    data_id = data[0]["id"]
    response = client.delete(f"/data/{data_id}")
    assert response.status_code == 200
