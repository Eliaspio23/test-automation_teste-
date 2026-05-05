import pytest

USERNAME = "auto_test_user"
PASSWORD = "pass123"
USER_PAYLOAD = {
    "id": 900001,
    "username": USERNAME,
    "firstName": "Auto",
    "lastName": "Test",
    "email": "autotest@example.com",
    "password": PASSWORD,
    "phone": "11999999999",
    "userStatus": 1,
}


def test_create_user(session, base_url):
    response = session.post(f"{base_url}/user", json=USER_PAYLOAD)
    assert response.status_code == 200


def test_login_user(session, base_url):
    response = session.get(
        f"{base_url}/user/login",
        params={"username": USERNAME, "password": PASSWORD},
    )
    assert response.status_code == 200
    assert "logged in" in response.json()["message"].lower()


def test_get_user(session, base_url):
    response = session.get(f"{base_url}/user/{USERNAME}")
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == USERNAME
    assert data["email"] == "autotest@example.com"


def test_update_user(session, base_url):
    updated = {**USER_PAYLOAD, "firstName": "Updated", "email": "updated@example.com"}
    response = session.put(f"{base_url}/user/{USERNAME}", json=updated)
    assert response.status_code == 200


def test_logout_user(session, base_url):
    response = session.get(f"{base_url}/user/logout")
    assert response.status_code == 200


def test_delete_user(session, base_url):
    response = session.delete(f"{base_url}/user/{USERNAME}")
    assert response.status_code == 200


def test_get_deleted_user_returns_404(session, base_url):
    response = session.get(f"{base_url}/user/{USERNAME}")
    assert response.status_code == 404
