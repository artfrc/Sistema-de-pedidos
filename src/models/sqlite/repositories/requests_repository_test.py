from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.entities.requests import RequestsTable
from src.models.sqlite.repositories.requests_repository import RequestsRepository

class MockRequestsTable:

    def __init__(self):
        self.request = RequestsTable(
            id=1,
            description="Request 1",
            user_id=1
        )

class MockConnection:

    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
            data = 
            [
                (
                    [mock.call.query(RequestsTable)],
                    [RequestsTable(id=1, description="Request 1", user_id=1)] 
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

def test_create_request():
    mock_connection = MockConnection()
    repo = RequestsRepository(mock_connection)
    request = MockRequestsTable().request
    repo.create_request(request)

    mock_connection.session.add.assert_called_once_with(request)
    mock_connection.session.commit.assert_called_once()

def test_get_request_by_id() -> RequestsTable:
    mock_connection = MockConnection()
    repo = RequestsRepository(mock_connection)
    response = repo.get_request_by_id(1)

    mock_connection.session.query.assert_called_once_with(RequestsTable)
    mock_connection.session.filter.assert_called_once_with(RequestsTable.id == 1)
    mock_connection.session.one.assert_called_once()

    assert response.id == 1
    assert response.description == "Request 1"
    assert response.user_id == 1

def test_list_requests():
    mock_connection = MockConnection()
    repo = RequestsRepository(mock_connection)
    response = repo.list_requests()

    mock_connection.session.query.assert_called_once_with(RequestsTable)
    mock_connection.session.all.assert_called_once()

    assert response[0].id == 1
    assert response[0].description == "Request 1"
    assert response[0].user_id == 1

def test_list_requests_no_result():
    mock_connection = MockConnectionNoResult()
    repo = RequestsRepository(mock_connection)
    response = repo.list_requests()

    mock_connection.session.query.assert_called_once_with(RequestsTable)
    mock_connection.session.all.assert_not_called()

    assert response == []

def test_delete_request():
    mock_connection = MockConnection()
    repo = RequestsRepository(mock_connection)
    repo.delete_request(1)

    mock_connection.session.query.assert_called_once_with(RequestsTable)
    mock_connection.session.filter.assert_called_once_with(RequestsTable.id == 1)
    mock_connection.session.delete.assert_called_once()
    mock_connection.session.commit.assert_called_once()

def test_delete_request_error():
    mock_connection_no_result = MockConnectionNoResult()
    repo = RequestsRepository(mock_connection_no_result)

    with pytest.raises(Exception):
        repo.delete_request(1)

    mock_connection_no_result.session.rollback.assert_called_once()
    