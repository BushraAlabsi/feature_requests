
import unittest
from flask import url_for, json
from baseTest import BaseTestCase
from feature_req.models import Client, ProductArea, Request


class FeatureRequestsTestCase(BaseTestCase):

    # Ensure that Flask was set up correctly
	def test_index(self):
		response = self.client.get('/', content_type='html/text')
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Feature Requests', response.data)

    # Ensure that main page loads when /requests is requested
	def test_requests_route(self):
		response = self.client.get('/request/getAll')
		self.assertIn(b'Feature Request Test', response.data)

    # Ensure that add new request page loads
	def test_add_request_route(self):
		response = self.client.get('/request/add', follow_redirects=True)
		self.assertIn(b'Request a new Feature', response.data)

	def test_feature_request_get_response(self):
		response = self.client.get("/request/getAll")
		#the example request in the database
		contents = ['Feature Request Test', 'Description', 'Billings', '1', 'Client C']
		for content in contents:
			self.assertIn(content, str(response.data))

	def test_feature_request_can_post(self):

		data = {'title': 'new title', 'description': 'description1', 'client_id': 2, 'priority': 1,
                'target_date': '2019-1-7', 'product_area_id': 4, 'form': ''}
       
		response= self.client.post(
			'/request/add',
	        headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
	        data=json.dumps(data),
	        follow_redirects=True
	    	)
		self.assertEqual(200, response.status_code)
			

	def test_feature_request_can_update(self):

		data = {'title': 'title1', 'description': 'description1', 'client_id': 2, 'priority': 3,
                'target_date': '2019-1-7', 'product_area_id': 4, 'form': ''}

		
		response= self.client.post(
			"request/edit/%d"%{self.request.id}.pop(),
	        headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
	        data=json.dumps(data),
	        follow_redirects=True
	        )
		self.assertEqual(200, response.status_code)
			

	def test_feature_request_can_delete(self):
		resp = self.client.delete("request/delete/%d"%{self.request.id}.pop())
		self.assertEqual(204, resp.status_code)

	def test_feature_request_get_client_requests_response(self):
		response = self.client.get("/request/get/1")
		#the example request in the database
		contents = ['Client B', 'Client C']
		for content in contents:
			self.assertNotIn(content, str(response.data))




if __name__ == '__main__':
    unittest.main()
