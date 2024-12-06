from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.users import UsersTable
from src.models.sqlite.interfaces.users_repository_interface import IUserRepository

class UserRepository(IUserRepository):
    def __init__(self, db_connection):
        self.__db_connection = db_connection

    def create_user(self, user: UsersTable):
        with self.__db_connection as database:
            try:
                database.session.add(user)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
            
    def get_user_by_id(self, user_id: int) -> UsersTable:
        with self.__db_connection as database:
            try:
                user = (
                    database.session
                    .query(UsersTable)
                    .filter(UsersTable.id == user_id)
                    .one()
                )
                return user
            except NoResultFound:
                return None

    def list_users(self) -> List[UsersTable]:
    
        with self.__db_connection as database:
            try:
                users = database.session.query(UsersTable).all()
                return users
            except NoResultFound:
                return []
            
    def delete_user(self, user_id: int):
        with self.__db_connection as database:
            try:
                (
                    database.session
                    .query(UsersTable)
                    .filter(UsersTable.id == user_id)
                    .delete()
                )
                database.session.commit()            
            except Exception as exception:
                database.session.rollback()
                raise exception

        