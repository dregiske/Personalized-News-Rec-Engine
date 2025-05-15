import pytest
from app.security import hash_password, verify_password, create_access_token
from app.config   import SECRET_KEY, ALGORITHM

def test_password_hash_and_verify():
    raw = "mypassword"
    hashed = hash_password(raw)
    assert hashed != raw
    assert verify_password(raw, hashed)

def test_jwt_roundtrip():
    data = {"sub": "bob@example.com"}
    token = create_access_token(data.copy())
    # You can decode with PyJWT directly
    import jwt
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    assert payload["sub"] == "bob@example.com"
    assert "exp" in payload
