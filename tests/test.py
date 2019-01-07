
import unittest
from flask import url_for, json
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

	def test_feature_request_get_response(self):
		response = self.client.get("/getRequests")
		#the example request in the database
		contents = ['Feature request', 'Description', 'Billings', '1', 'Client C']
		for content in contents:
			self.assertIn(content, str(response.data))

	def test_feature_request_can_delete(self):
		resp = self.client.delete("req/%d"%{self.request.id}.pop())
		self.assertEqual(204, resp.status_code)

	def test_feature_request_post_success(self):
        # url = url_for('api.featurerequestresourcelist', _external=True)

		data = {'title': 'title1', 'description': 'description1', 'client': 'Client C', 'priority': 3,
                'target_date': '2019-1-7', 'product_area': 'product_area', 'form': ''}

		response = self.client.post(
			'/addRequest',
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
            data=json.dumps(data),
            follow_redirects=True
            )
		self.assertIn(b'description1', response.data)




if __name__ == '__main__':
    unittest.main()
