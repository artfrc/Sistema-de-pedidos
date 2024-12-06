import pytest
from src.models.sqlite.entities.requests import RequestsTable
from src.models.sqlite.settings.connection import db_connection_handler
from .requests_repository import RequestsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Interacts with the database")
def test_list_requests():
    repo = RequestsRepository(db_connection_handler)
    response = repo.list_requests()

    response_expected = [
        {"id":1, "description": "Request 1", "user_id": 1},
        {"id":2, "description": "Request 2", "user_id": 1},
        {"id":3, "description": "Request 3", "user_id": 2},
        {"id":4, "description": "Request 4", "user_id": 2}
    ]

    response_as_dict = [
        {"id": request.id, "description": request.description, "user_id": request.user_id}
        for request in response
    ]

    assert response_as_dict == response_expected

@pytest.mark.skip(reason="Interacts with the database")
def test_get_request_by_id(request_id: int = 1) -> RequestsTable:
    repo = RequestsRepository(db_connection_handler)
    response = repo.get_request_by_id(request_id)

    print()
    print(response)

    response_expected = [
         {"id": 1, "description": "Request 1", "user_id": 1}
    ]

    response_as_dict = [
        {"id": response.id, "description": response.description, "user_id": response.user_id}
    ]
    
    assert response_as_dict == response_expected