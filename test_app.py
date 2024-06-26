import pytest
from flask import session
from app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_index(app, client):
    res = client.get('/')
    print(res.data)
    assert res.status_code == 200


def test_game(app, client):
    client.get('/')
    res = client.post('/game', data={'cell': '0-0'})
    assert res.status_code == 200
    assert "game_over" in session
