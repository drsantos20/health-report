import json

from app.api import crud


def test_create_note(test_app, monkeypatch):
    test_request_payload = {
        "country": "Brazil",
        "state": "",
        "confirmed": 1,
        "deaths": 20,
        "recovered": 1,
    }
    test_response_payload = {
        "id": 1,
        "country": "Brazil",
        "state": "",
        "confirmed": 1,
        "deaths": 20,
        "recovered": 1,
    }

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(crud, "post", mock_post)

    response = test_app.post(
        "/covid_report/",
        data=json.dumps(test_request_payload),
    )

    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_create_note_invalid_json(test_app):
    response = test_app.post("/covid_report/", data=json.dumps({"country": "Brazil"}))
    assert response.status_code == 422


def test_read_note(test_app, monkeypatch):
    test_data = {
        "id": 1,
        "country": "Brazil",
        "state": "",
        "confirmed": 1,
        "deaths": 20,
        "recovered": 1,
    }

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/covid_report/1")
    assert response.status_code == 200
    assert response.json() == test_data


def test_read_note_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/covid_report/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Report not found"


def test_read_all_notes(test_app, monkeypatch):
    test_data = [
        {"country": "Brazil", "state": "", "confirmed": 1, "deaths": 20, "recovered": 1, "id": 1},
        {"country": "Brazil", "state": "", "confirmed": 1, "deaths": 20, "recovered": 1, "id": 2},
    ]

    async def mock_get_all():
        return test_data

    monkeypatch.setattr(crud, "get_all", mock_get_all)

    response = test_app.get("/covid_report/")
    assert response.status_code == 200
    assert response.json() == test_data
