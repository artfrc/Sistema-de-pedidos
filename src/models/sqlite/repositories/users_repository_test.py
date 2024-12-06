from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.users import UsersTable
from .users_repository import UserRepository

class MockConnection:

    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
            data = 
            [
                (
                    [mock.call.query(UsersTable)], # query
                    [UsersTable(id=1, name="John Doe", username="johndoe")] # resultado
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def test_list_users():
    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)
    response = repo.list_users()

    mock_connection.session.query.assert_called_once_with(UsersTable)
    mock_connection.session.all.assert_called_once_with()

    assert response[0].id == 1
    assert response[0].name == "John Doe"
    assert response[0].username == "johndoe"