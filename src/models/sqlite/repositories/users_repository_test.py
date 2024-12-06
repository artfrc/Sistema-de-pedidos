from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.users import UsersTable
from .users_repository import UserRepository

class MockUsersTable:
    
    def __init__(self):
        self.user = UsersTable(
            id=1,
            name="John Doe",
            username="johndoe",
            password="123456"
        )

class MockConnection:

    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
            data = 
            [
                (
                    [mock.call.query(UsersTable)],
                    [UsersTable(id=1, name="John Doe", username="johndoe")] 
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

class MockConnectionNoResult:

    def __init__(self):
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs): 
        raise NoResultFound("No result found")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def test_create_user():
    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)
    user = MockUsersTable().user
    repo.create_user(user)

    mock_connection.session.add.assert_called_once_with(user)
    mock_connection.session.commit.assert_called_once()

def test_get_user_by_id() -> UsersTable:
    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)
    user = MockUsersTable().user
    response = repo.get_user_by_id(user.id)

    mock_connection.session.query.assert_called_once_with(UsersTable)
    mock_connection.session.filter.assert_called_once_with(UsersTable.id == user.id)
    mock_connection.session.one.assert_called_once()

    assert response.id == 1
    assert response.name == "John Doe"
    assert response.username == "johndoe"

def test_list_users():
    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)
    response = repo.list_users()

    mock_connection.session.query.assert_called_once_with(UsersTable)
    mock_connection.session.all.assert_called_once_with()

    assert response[0].id == 1
    assert response[0].name == "John Doe"
    assert response[0].username == "johndoe"

def test_list_users_no_result():
    mock_connection_no_result = MockConnectionNoResult()
    repo = UserRepository(mock_connection_no_result)
    response = repo.list_users()

    mock_connection_no_result.session.query.assert_called_once_with(UsersTable)
    mock_connection_no_result.session.all.assert_not_called()

    assert response == []

def test_delete_user():
    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.delete_user(1)

    mock_connection.session.query.assert_called_once_with(UsersTable)
    mock_connection.session.filter.assert_called_once_with(UsersTable.id == 1)
    mock_connection.session.delete.assert_called_once_with()
    mock_connection.session.commit.assert_called_once_with()

def test_delete_user_error():
    mock_connection_no_result = MockConnectionNoResult()
    repo = UserRepository(mock_connection_no_result)

    with pytest.raises(Exception):
        repo.delete_user(1)

    mock_connection_no_result.session.rollback.assert_called_once()
