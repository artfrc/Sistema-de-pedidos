import pytest
from sqlalchemy.engine import Engine
from .connection import db_connection_handler

@pytest.mark.skip(reason="Interacts with the database")
def test_connection():

    assert db_connection_handler.get_engine() is  None   

    db_connection_handler.connect_to_db()
    engine = db_connection_handler.get_engine()

    assert engine is not None
    assert isinstance(engine, Engine)