"""Helper utilities for testing."""

import os
import shutil
import socket


from config import get_settings
from database import Base, init_engine, get_session


class BaseTestCase:
    def setup_class(self):
        os.environ["env"] = "test"
        settings = get_settings(env="test")

        # reinitialize the database engine to use the test database
        self.engine = init_engine(settings.SQLALCHEMY_DATABASE_URI)
        Base.metadata.create_all(self.engine)
        self.session = get_session(self.engine)

    def teardown_class(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def teardown_method(self):
        self.session.rollback()
