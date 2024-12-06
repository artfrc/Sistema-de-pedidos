from sqlalchemy import BIGINT, Column, String
from src.models.sqlite.settings.base import Base

class UsersTable(Base):

    __tablename__ = 'users'
    id = Column(BIGINT, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f"Users: [id: {self.id}, name: {self.name}, username: {self.username}]"