import pytest

@pytest.mark.asyncio
async def test_signup_and_login(client_override):
    # client_override is already an AsyncClient instance
    client = client_override

    # 1) Sign up
    resp = await client.post(
        "/auth/signup",
        json={"email": "alice@example.com", "password": "secret123"}
    )
    assert resp.status_code == 201
    body = resp.json()
    assert body["email"] == "alice@example.com"
    assert "id" in body

    # 2) Duplicate should fail
    resp2 = await client.post(
        "/auth/signup",
        json={"email": "alice@example.com", "password": "secret123"}
    )
    assert resp2.status_code == 400

    # 3) Login
    resp3 = await client.post(
        "/auth/token",
        data={"username": "alice@example.com", "password": "secret123"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert resp3.status_code == 200
    token_data = resp3.json()
    assert "access_token" in token_data
    assert token_data["token_type"] == "bearer"

    # 4) Access protected endpoint
    headers = {"Authorization": f"Bearer {token_data['access_token']}"}
    resp4 = await client.get("/me", headers=headers)
    assert resp4.status_code == 200
    assert resp4.json()["email"] == "alice@example.com"
