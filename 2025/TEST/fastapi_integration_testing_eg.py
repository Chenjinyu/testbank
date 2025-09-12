"""
Integration testing example for FastAPI application using TestClient.
Purpose:
1. Tests how multiple components work together.
2. Example: DB + API layer, or two microservices interacting.
3. Usually interacts with external resources (DB, network), but in a controlled/test evironment.
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from myapp.app import app
from myapp.db import get_db, Base # from sqlalchemy.ext.declarative import declarative_base and assgin the base with declarative_base()


# Setup test DB
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"  # Using SQLite for simplicity or sqlite:///./test.db for file-based
engine = create_engine(url=SQLALCHEMY_DATABASE_URL)
testing_session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = Base.metadata.create_all(bind=engine) # create schema to the binded engine DB


# override get db dependency
def override_get_db():
    db = testing_session_local()
    try:
        yield db
    finally:
        db.close()  
        
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_item():
    response = client.post("/items/", json={"name": "Test Item", "description": "A test item", "price": 10.5, "tax": 1.5})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["description"] == "A test item"
    assert data["price"] == 10.5
    assert data["tax"] == 1.5
    assert "id" in data


