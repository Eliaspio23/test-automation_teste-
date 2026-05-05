import pytest

ORDER_ID = 900001
ORDER_PAYLOAD = {
    "id": ORDER_ID,
    "petId": 1,
    "quantity": 2,
    "status": "placed",
    "complete": False,
}


def test_get_inventory(session, base_url):
    response = session.get(f"{base_url}/store/inventory")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_place_order(session, base_url):
    response = session.post(f"{base_url}/store/order", json=ORDER_PAYLOAD)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == ORDER_ID
    assert data["status"] == "placed"
    assert data["quantity"] == 2


def test_get_order_by_id(session, base_url):
    response = session.get(f"{base_url}/store/order/{ORDER_ID}")
    assert response.status_code == 200
    assert response.json()["id"] == ORDER_ID


def test_delete_order(session, base_url):
    response = session.delete(f"{base_url}/store/order/{ORDER_ID}")
    assert response.status_code == 200


def test_get_deleted_order_returns_404(session, base_url):
    response = session.get(f"{base_url}/store/order/{ORDER_ID}")
    assert response.status_code == 404
