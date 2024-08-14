import unittest
from backend.app import create_app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_wallet(self):
        response = self.client.post('/wallet/create', json={'user_id': '123'})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
