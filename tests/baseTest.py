from flask_testing import TestCase
from datetime import datetime
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
        self.request= Request(
            title='Feature Request Test',
            description='Description',
            target_date= datetime.strptime('Jan 1 2019', '%b %d %Y'),
            client_priority=1,
            product_area_id=2,
            client_id=3
        )
        db.session.add(self.request)
    	db.session.commit()
        request= Request(
            title='Second Request Test',
            description='Description II',
            target_date= datetime.strptime('Jan 15 2019', '%b %d %Y'),
            client_priority=1,
            product_area_id=2,
            client_id=1
        )
        db.session.add(request)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


