from sqlalchemy.orm.exc import NoResultFound
from typing import List
from src.models.sqlite.entities.requests import RequestsTable

class RequestsRepository:

    def __init__(self, db_connection):
        self.__db_connection = db_connection

    def create_request(self, request: RequestsTable):
        with self.__db_connection as database:
            try:
                database.session.add(request)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
            
    def get_request_by_id(self, request_id: int) -> RequestsTable:
        with self.__db_connection as database:
            try:
                request = (
                    database.session
                    .query(RequestsTable)
                    .filter(RequestsTable.id == request_id)
                    .one()
                )
                return request
            except NoResultFound:
                return None
            
    def list_requests(self) -> List[RequestsTable]:
        with self.__db_connection as database:
            try:
                requests = database.session.query(RequestsTable).all()
                return requests
            except NoResultFound:
                return []
            
    def delete_request(self, request_id: int):
        with self.__db_connection as database:
            try:
                (
                    database.session
                    .query(RequestsTable)
                    .filter(RequestsTable.id == request_id)
                    .delete()
                )
                database.session.commit()            
            except Exception as exception:
                database.session.rollback()
                raise exception
        
