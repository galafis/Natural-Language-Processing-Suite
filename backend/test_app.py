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
        self.assertIn('version', data)
        self.assertIn('timestamp', data)

    def test_process_text_success(self):
        response = self.app.post('/api/process',
                                 data=json.dumps({'text': 'Hello World'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('original_text', data)
        self.assertIn('processed_text', data)
        self.assertEqual(data['original_text'], 'Hello World')
        self.assertEqual(data['processed_text'], 'Processed: HELLO WORLD')

    def test_process_text_missing_data(self):
        response = self.app.post('/api/process',
                                 data=json.dumps({}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)

    def test_process_text_no_json(self):
        response = self.app.post('/api/process')
        # Flask returns 415 when Content-Type is not application/json
        self.assertIn(response.status_code, [400, 415])

    def test_analytics(self):
        response = self.app.get('/api/analytics')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('analytics_data', data)

    def test_upload(self):
        response = self.app.post('/api/upload')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('message', data)

if __name__ == '__main__':
    unittest.main()
