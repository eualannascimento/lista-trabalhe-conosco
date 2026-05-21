import logging
import unittest
from unittest.mock import MagicMock, patch

import requests

from src.py.functions.website_verification import (
    verify_website_status,
    verify_websites_concurrent,
)

logging.disable(logging.CRITICAL)


class TestWebsiteVerification(unittest.TestCase):
    def _session_ok(self, status=200):
        session = MagicMock()
        session.head.return_value = MagicMock(status_code=status)
        session.close = MagicMock()
        return session

    @patch("src.py.functions.website_verification.create_shared_session")
    def test_verify_website_status_success(self, mock_create):
        mock_create.return_value = self._session_ok(200)

        result = verify_website_status("http://example.com")
        self.assertEqual(result["status"], "1")
        self.assertEqual(result["status_code"], 200)
        self.assertIsNone(result["error"])

    @patch("src.py.functions.website_verification.create_shared_session")
    def test_verify_website_status_failure_404(self, mock_create):
        session = MagicMock()
        session.head.return_value = MagicMock(status_code=404)
        session.get.return_value = MagicMock(status_code=404)
        session.close = MagicMock()
        mock_create.return_value = session

        result = verify_website_status("http://example.com/404")
        self.assertEqual(result["status"], "0")
        self.assertIn("404", result["error"])

    @patch("src.py.functions.website_verification.create_shared_session")
    def test_verify_website_status_exception(self, mock_create):
        session = MagicMock()
        session.head.side_effect = requests.exceptions.ConnectionError("Connection error")
        session.close = MagicMock()
        mock_create.return_value = session

        result = verify_website_status("http://example.com/error")
        self.assertEqual(result["status"], "0")
        self.assertIn("Connection error", result["error"])

    @patch("src.py.functions.website_verification.verify_website_status")
    def test_verify_websites_concurrent(self, mock_verify):
        def side_effect(session, url, timeout=15):
            if "success" in url:
                return {"status": "1", "status_code": 200, "error": None}
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
