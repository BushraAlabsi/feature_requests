
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

    # Ensure that add new request page loads
	def test_add_request_route(self):
		response = self.client.get('/addRequest', follow_redirects=True)
		self.assertIn(b'Request a new Feature', response.data)

	#Ensure that requests are returned correctly
	def test_feature_request_get_response(self):
		response = self.client.get("/getRequests")
		#the example request in the database
		contents = ['Feature request', 'Description', 'Billings', '1', 'Client C']
		for content in contents:
			self.assertIn(content, str(response.data))




if __name__ == '__main__':
    unittest.main()
