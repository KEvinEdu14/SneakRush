import unittest
from main import app

class CreateCategoryTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_create_category(self):
        response = self.client.post('/categories', json={
            "name": "Fútbol",
            "description": "Deportes para fútbol"
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
