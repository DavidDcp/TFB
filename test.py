def test_insert_data(client):
    response = client.post("/data", json={"name": "Test"})
    assert response.status_code == 200

def test_get_all_data(client):
    client.post("/data", json={"name": "User1"})
    client.post("/data", json={"name": "User2"})
    response = client.get("/data")
    assert response.status_code == 200
    assert len(response.json) == 2

def test_delete_data(client):
    client.post("/data", json={"name": "DeleteMe"})
    data = client.get("/data").json
    data_id = data[0]["id"]
    response = client.delete(f"/data/{data_id}")
    assert response.status_code == 200
