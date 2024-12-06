from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.users import UsersTable

class UserRepository:
    def __init__(self, db_connection):
        self.__db_connection = db_connection

    def list_users(self) -> List[UsersTable]:
        # No with entramos na função __enter__ do objeto self.__db_connection e o retorno é atribuído a variável database
        with self.__db_connection as database:
            try:
                users = database.session.query(UsersTable).all()
                return users
            except NoResultFound:
                return []

        