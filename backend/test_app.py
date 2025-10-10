import unittest
import json
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<!DOCTYPE html>", response.data)
        self.assertIn(b"Natural-Language-Processing-Suite", response.data)

        

    def test_status(self):
        response = self.app.get('/api/status')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'running')

if __name__ == '__main__':
    unittest.main()

