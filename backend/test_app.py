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
        self.assertIn('endpoints', data)

    def test_process_text_success(self):
        response = self.app.post('/api/process',
                                 data=json.dumps({'text': 'Hello World'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('original_text', data)
        self.assertIn('processed_text', data)
        self.assertIn('length', data)
        self.assertIn('timestamp', data)
        self.assertEqual(data['original_text'], 'Hello World')
        self.assertEqual(data['processed_text'], 'Processed: HELLO WORLD')
        self.assertEqual(data['length'], 11)

    def test_process_text_missing_data(self):
        response = self.app.post('/api/process',
                                 data=json.dumps({}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)

    def test_process_text_no_json(self):
        response = self.app.post('/api/process')
        # Should return 400 for invalid/missing JSON
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

    def test_process_text_invalid_type(self):
        response = self.app.post('/api/process',
                                 data=json.dumps({'text': 123}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)

    def test_process_text_too_long(self):
        long_text = 'a' * 10001
        response = self.app.post('/api/process',
                                 data=json.dumps({'text': long_text}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)
        self.assertIn('too long', data['error'].lower())

    def test_not_found(self):
        response = self.app.get('/api/nonexistent')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()
