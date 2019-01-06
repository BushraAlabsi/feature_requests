from flask_testing import TestCase

from feature_req import create_app, db
from feature_req.models import Client, ProductArea, Request
from tests.config import TestConfig

class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        return create_app(TestConfig)

    def setUp(self):
        db.create_all(None)
        db.session.add(Client(name='Client A'))
        db.session.add(Client(name='Client B'))
    	db.session.add(Client(name='Client C'))
    	db.session.commit()
        db.session.add(ProductArea(name='Policies'))
        db.session.add(ProductArea(name='Billings'))
        db.session.add(ProductArea(name='Claims'))
    	db.session.add(ProductArea(name='Reports'))
    	db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


