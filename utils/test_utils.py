"""Helper utilities for testing."""

import os


from config import get_settings
from database import Base, init_engine, db_session, init_db, drop_db


class BaseTestCase:
    def setup_method(self):
        os.environ["env"] = "test"
        settings = get_settings(env="test")

        # reinitialize the database engine to use the test database
        self.engine = init_engine(settings.SQLALCHEMY_DATABASE_URI)
        init_db()
        self.session = db_session

    def teardown_method(self):
        self.session.close()
        drop_db()
        self.session.remove()

    

    # def teardown_method(self):
    #     self.session.rollback()
