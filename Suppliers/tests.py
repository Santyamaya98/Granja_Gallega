from django.test import TestCase
import requests

BASE_URL = "http://127.0.0.1:8000"


def get_token(username, password):
    url = f"{BASE_URL}/api/token/"
    data = {"username": username, "password": password}
    response = requests.post(url, data=data)

    if response.status_code == 200:
        tokens = response.json()
        print("✅ Token generated successfully")
        return tokens.get("access"), tokens.get("refresh")
    else:
        print("❌ Failed to get token:", response.text)
        return None, None


class SupplierAPITest(TestCase):
    """Integration test for /api/suppliers/ using JWT authentication"""

    def setUp(self):
        # You can use your Django superuser credentials here
        self.username = "admin"
        self.password = "admin"
        self.access_token, self.refresh_token = get_token(self.username, self.password)

    def test_suppliers_endpoint(self):
        """Check if /api/suppliers/ returns 200 with valid token"""
        self.assertIsNotNone(self.access_token, "Access token not generated")

        url = f"{BASE_URL}/api/suppliers/"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        response = requests.get(url, headers=headers)

        print(f"\n🔍 GET {url}")
        print(f"Status Code: {response.status_code}")

        # Assertions
        self.assertEqual(response.status_code, 200, "API did not return 200 OK")

        try:
            data = response.json()
            print("Response JSON:", data)
        except Exception:
            print("Response Text:", response.text)
