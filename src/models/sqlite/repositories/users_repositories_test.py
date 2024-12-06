import pytest
from src.models.sqlite.entities.users import UsersTable
from src.models.sqlite.settings.connection import db_connection_handler
from .users_repository import UserRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Interacts with the database")
def test_list_users():
    repo = UserRepository(db_connection_handler)
    response = repo.list_users()

    response_expected = [
        {"id": 1, "name": "John Doe", "username": "johndoe"},
        {"id": 2, "name": "Jane Doe", "username": "janedoe"},
    ]

    response_as_dict = [
        {"id": user.id, "name": user.name, "username": user.username}
        for user in response
    ]

    assert response_as_dict == response_expected

@pytest.mark.skip(reason="Interacts with the database")
def test_get_user_by_id(user_id: int = 1) -> UsersTable:
    repo = UserRepository(db_connection_handler)
    response = repo.get_user_by_id(user_id)

    response_expected = [
         {"id": 1, "name": "John Doe", "username": "johndoe"}
    ]

    response_as_dict = [
        {"id": response.id, "name": response.name, "username": response.username}
    ]
    
    assert response_as_dict == response_expected