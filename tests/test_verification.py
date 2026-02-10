import logging
import unittest
from unittest.mock import MagicMock, patch

from src.py.functions.website_verification import (
    verify_website_status,
    verify_websites_concurrent,
)

# Disable logging during tests
logging.disable(logging.CRITICAL)

class TestWebsiteVerification(unittest.TestCase):
    @patch("src.py.functions.website_verification.requests.get")
    def test_verify_website_status_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        result = verify_website_status("http://example.com")
        self.assertEqual(result["status"], "1")
        self.assertEqual(result["status_code"], 200)
        self.assertIsNone(result["error"])

    @patch("src.py.functions.website_verification.requests.get")
    def test_verify_website_status_failure_404(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = verify_website_status("http://example.com/404")
        self.assertEqual(result["status"], "0")
        self.assertIn("404", result["error"])

    @patch("src.py.functions.website_verification.requests.get")
    def test_verify_website_status_exception(self, mock_get):
        mock_get.side_effect = Exception("Connection error")

        result = verify_website_status("http://example.com/error")
        self.assertEqual(result["status"], "0")
        self.assertIn("Connection error", result["error"])

    @patch("src.py.functions.website_verification.verify_website_status")
    def test_verify_websites_concurrent(self, mock_verify):
        # Mock behavior for concurrent test
        def side_effect(url, timeout=15):
            if "success" in url:
                return {"status": "1", "status_code": 200, "error": None}
            else:
                return {"status": "0", "status_code": 404, "error": "Not Found"}
        
        mock_verify.side_effect = side_effect

        items = [
            {"URL": "http://success.com", "Nome da Empresa": "Success Corp"},
            {"URL": "http://fail.com", "Nome da Empresa": "Fail Corp"},
        ]

        failed_items = verify_websites_concurrent(items)
        
        self.assertEqual(len(failed_items), 1)
        self.assertEqual(failed_items[0]["Nome da Empresa"], "Fail Corp")
        self.assertEqual(items[1]["Status da URL"], "0")
        self.assertEqual(items[0]["Status da URL"], "1")


if __name__ == "__main__":
    unittest.main()
