## base.py
from flask_testing import TestCase

from feature_req import create_app, db
from feature_req.models import Client, ProductArea, Request
from tests.config import TestConfig

class BaseTestCase(TestCase):
    """A base test case."""

    def create_app1(self):
        return create_app(TestConfig)

    def setUp(self):
        db.create_all(None)
    	client=Client(name='Client A')
    	db.session.add(client)
    	db.session.commit()
    	client=Client(name='Client B')
    	db.session.add(client)
    	db.session.commit()
    	client=Client(name='Client C')
    	db.session.add(client)
    	db.session.commit()
    	area=ProductArea(name='Policies')
    	db.session.add(area)
    	db.session.commit()
    	area=ProductArea(name='Billings')
    	db.session.add(area)
    	db.session.commit()
    	area=ProductArea(name='Claims')
    	db.session.add(area)
    	db.session.commit()
    	area=ProductArea(name='Reports')
    	db.session.add(area)
    	db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

# tests/test_basic.py

# import unittest

# from base import BaseTestCase


# class FlaskTestCase(BaseTestCase):

#     # Ensure that Flask was set up correctly
#     def test_index(self):
#         response = self.client.get('/login', content_type='html/text')
#         self.assertEqual(response.status_code, 200)

#     # Ensure that main page requires user login
#     def test_main_route_requires_login(self):
#         response = self.client.get('/', follow_redirects=True)
#         self.assertIn(b'Please log in to access this page', response.data)

#     # Ensure that welcome page loads
#     def test_welcome_route_works_as_expected(self):
#         response = self.client.get('/welcome', follow_redirects=True)
#         self.assertIn(b'Welcome to Flask!', response.data)

#     # Ensure that posts show up on the main page
#     def test_posts_show_up_on_main_page(self):
#         response = self.client.post(
#             '/login',
#             data=dict(username="admin", password="admin"),
#             follow_redirects=True
#         )
#         self.assertIn(b'This is a test. Only a test.', response.data)


# if __name__ == '__main__':
#     unittest.main()

# # tests/test_blog.py

# import unittest

# from base import BaseTestCase


# class BlogPostTests(BaseTestCase):

#     # Ensure a logged in user can add a new post
#     def test_user_can_post(self):
#         with self.client:
#             self.client.post(
#                 '/login',
#                 data=dict(username="admin", password="admin"),
#                 follow_redirects=True
#             )
#             response = self.client.post(
#                 '/',
#                 data=dict(title="test", description="test"),
#                 follow_redirects=True
#             )
#             self.assertEqual(response.status_code, 200)
#             self.assertIn(b'New entry was successfully posted. Thanks.',
#                           response.data)


# if __name__ == '__main__':
#     unittest.main()