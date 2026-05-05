import pytest

PET_ID = 900001
PET_PAYLOAD = {
    "id": PET_ID,
    "name": "Rex",
    "status": "available",
    "photoUrls": ["http://example.com/rex.jpg"],
}


def test_create_pet(session, base_url):
    response = session.post(f"{base_url}/pet", json=PET_PAYLOAD)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == PET_ID
    assert data["name"] == "Rex"
    assert data["status"] == "available"


def test_get_pet_by_id(session, base_url):
    response = session.get(f"{base_url}/pet/{PET_ID}")
    assert response.status_code == 200
    assert response.json()["id"] == PET_ID


def test_find_pets_by_status(session, base_url):
    response = session.get(f"{base_url}/pet/findByStatus", params={"status": "available"})
    assert response.status_code == 200
    pets = response.json()
    assert isinstance(pets, list)
    assert all(p["status"] == "available" for p in pets if "status" in p)


def test_update_pet(session, base_url):
    updated = {**PET_PAYLOAD, "name": "Rex Updated", "status": "pending"}
    response = session.put(f"{base_url}/pet", json=updated)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Rex Updated"
    assert data["status"] == "pending"


def test_delete_pet(session, base_url):
    response = session.delete(f"{base_url}/pet/{PET_ID}")
    assert response.status_code == 200


def test_get_deleted_pet_returns_404(session, base_url):
    response = session.get(f"{base_url}/pet/{PET_ID}")
    assert response.status_code == 404
