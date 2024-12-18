from sqlalchemy import BIGINT, Column, String, ForeignKey
from src.models.sqlite.settings.base import Base

class RequestsTable(Base):

    __tablename__ = 'requests'
    id = Column(BIGINT, primary_key=True)
    description = Column(String)
    user_id = Column(BIGINT, ForeignKey('users.id'), nullable=False)

    def __init__(self, description: str, user_id: int):
        self.description = description
        self.user_id = user_id

    def __repr__(self):
        return f"Requests: [id: {self.id}, description: {self.description}, user_id: {self.user_id}]"