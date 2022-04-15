from app import app_web
import unittest

class TestNoAuthenticationRequests(unittest.TestCase):
        
    # Testando se a resposta é 200 (ok)
    def test_get_all(self):
        app = app_web.test_client()
        self.response = app.get('/usuarios')
        self.assertEqual(200, self.response.status_code)
        
    def test_get_users_by_ID(self):
        app = app_web.test_client()
        self.response = app.get('/usuarios/1')
        self.assertEqual(200, self.response.status_code)
    