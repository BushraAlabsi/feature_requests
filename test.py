from feature_req import create_app
import unittest

app = create_app()

class FlaskTestCase(unittest.TestCase):
	
	def test_index(self):
		tester= app.test_client(self)
		response= tester.get('/',content_type='htmt/text')
		self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
	unittest.main()