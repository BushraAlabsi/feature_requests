
import unittest

from baseTest import BaseTestCase


class FeatureRequestsTestCase(BaseTestCase):

    # Ensure that Flask was set up correctly
	def test_index(self):
		response = self.client.get('/', content_type='html/text')
		self.assertEqual(response.status_code, 200)

    # Ensure that main page loads when /requests is requested
	def test_requests_route(self):
		response = self.client.get('/requests')
		self.assertIn(b'Feature Requests', response.data)



if __name__ == '__main__':
    unittest.main()
