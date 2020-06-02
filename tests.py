import unittest
import json
from server import app

class TestNameMicroservice(unittest.TestCase):
    """Test that naming microservice works as expected."""

    def setUp(self):
        """Create test client before for each test."""

        self.client = app.test_client()
        app.config["TESTING"] = True


    def test_valid_input(self):
        """Test that microservice works with valid input."""

        res = self.client.post("/", data=json.dumps({"name": "peter"}),
                               content_type="application/json")
        data = res.json
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["age"], 57)


    def test_invalid_input(self):
        """Test that microservice returns None values given invalid name."""

        res = self.client.post("/", data=json.dumps({"name": "jlkajsdflkajs"}),
                               content_type="application/json")
        data = res.json
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["age"], None)


    def test_digit_input(self):
        """Test that microservice sends error when given digit as name."""

        res = self.client.post("/", data=json.dumps({"name": "3"}),
                               content_type="application/json")
        data = res.json
        self.assertEqual(res.status_code, 400)
        self.assertIn("error", data)


if __name__ == "__main__":
    unittest.main()
