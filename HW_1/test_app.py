import os
import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "healthy"})

    def test_index_reads_env_var(self):
        os.environ["APP_MESSAGE"] = "Test Custom Message"
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["message"], "Test Custom Message")

    def test_courses_endpoint(self):
        response = self.client.get("/courses")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(any(c["code"] == "CENG413" for c in data["courses"]))

if __name__ == "__main__":
    unittest.main()