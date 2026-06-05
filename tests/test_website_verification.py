from unittest.mock import patch, MagicMock

import pytest
import requests

from src.py.functions.website_verification import (
    _is_success,
    verify_website_status,
    verify_websites_concurrent,
)


class TestIsSuccess:
    def test_200_is_success(self):
        assert _is_success(200) is True

    def test_201_is_success(self):
        assert _is_success(201) is True

    def test_301_redirect_is_success(self):
        assert _is_success(301) is True

    def test_302_redirect_is_success(self):
        assert _is_success(302) is True

    def test_400_is_not_success(self):
        assert _is_success(400) is False

    def test_403_is_success(self):
        assert _is_success(403) is True

    def test_404_is_not_success(self):
        assert _is_success(404) is False

    def test_500_is_not_success(self):
        assert _is_success(500) is False

    def test_199_is_not_success(self):
        assert _is_success(199) is False

    def test_406_is_success(self):
        from src.py.functions.website_verification import _check_status

        # 406 é tratado como proteção anti-bot (WAF), portanto considerado válido
        assert _check_status(406, "https://boards.greenhouse.io/nubank") is True
        assert _check_status(406, "https://example.com") is True

    def test_429_is_success(self):
        from src.py.functions.website_verification import _check_status

        assert _check_status(429, "https://example.com") is True


class TestVerifyWebsiteStatus:
    def _mock_session(self, head_status=200, get_status=None, head_error=None):
        session = MagicMock()
        if head_error:
            session.head.side_effect = head_error
        else:
            session.head.return_value = MagicMock(status_code=head_status)
        if get_status is not None:
            session.get.return_value = MagicMock(status_code=get_status)
        session.close = MagicMock()
        return session

    @patch("src.py.functions.website_verification.create_shared_session")
    def test_success_on_200(self, mock_create):
        mock_create.return_value = self._mock_session(head_status=200)

        result = verify_website_status("https://example.com", retries=1)
        assert result["status"] == "1"
        assert result["status_code"] == 200
        assert result["error"] is None

    @patch("src.py.functions.website_verification.create_shared_session")
    def test_success_on_301(self, mock_create):
        mock_create.return_value = self._mock_session(head_status=301)

        result = verify_website_status("https://example.com", retries=1)
        assert result["status"] == "1"

    @patch("src.py.functions.website_verification.create_shared_session")
    def test_failure_on_404(self, mock_create):
        mock_create.return_value = self._mock_session(head_status=404, get_status=404)

        result = verify_website_status("https://example.com", retries=1)
        assert result["status"] == "0"
        assert "404" in result["error"]

    @patch("src.py.functions.website_verification.create_shared_session")
    def test_failure_on_connection_error(self, mock_create):
        mock_create.return_value = self._mock_session(
            head_error=requests.exceptions.ConnectionError("Connection refused")
        )

        result = verify_website_status("https://example.com", retries=1)
        assert result["status"] == "0"
        assert result["error"] is not None

    @patch("src.py.functions.website_verification.create_shared_session")
    def test_failure_on_timeout(self, mock_create):
        mock_create.return_value = self._mock_session(
            head_error=requests.exceptions.Timeout("Timed out")
        )

        result = verify_website_status("https://example.com", retries=1)
        assert result["status"] == "1"

    @patch("src.py.functions.website_verification.create_shared_session")
    def test_retries_on_failure(self, mock_create):
        session = MagicMock()
        session.head.side_effect = requests.exceptions.ConnectionError("fail")
        session.close = MagicMock()
        mock_create.return_value = session

        verify_website_status("https://example.com", retries=2, timeout=1)
        assert session.head.call_count == 2

    @patch("src.py.functions.website_verification.create_shared_session")
    def test_success_on_second_attempt(self, mock_create):
        session = MagicMock()
        session.head.side_effect = [
            MagicMock(status_code=500),
            MagicMock(status_code=200),
        ]
        session.close = MagicMock()
        mock_create.return_value = session

        result = verify_website_status("https://example.com", retries=2)
        assert result["status"] == "1"

    @patch("src.py.functions.website_verification.create_shared_session")
    def test_ssl_fallback_on_ssl_error(self, mock_create):
        session = MagicMock()
        session.head.side_effect = requests.exceptions.SSLError("SSL error")
        session.close = MagicMock()
        mock_create.return_value = session

        result = verify_website_status("https://example.com", retries=1)
        assert result["status"] == "1"

    @patch("src.py.functions.website_verification.create_shared_session")
    def test_returns_dict_structure(self, mock_create):
        mock_create.return_value = self._mock_session(head_status=200)

        result = verify_website_status("https://example.com", retries=1)
        assert "status" in result
        assert "status_code" in result
        assert "error" in result


class TestVerifyWebsitesConcurrent:
    @patch("src.py.functions.website_verification.verify_website_status")
    def test_updates_status_in_items(self, mock_verify):
        mock_verify.return_value = {"status": "1", "status_code": 200, "error": None}
        items = [
            {"Nome da Empresa": "A", "URL": "https://a.com", "Status da URL": "0"},
            {"Nome da Empresa": "B", "URL": "https://b.com", "Status da URL": "0"},
        ]

        verify_websites_concurrent(items, max_workers=2)
        assert all(item["Status da URL"] == "1" for item in items)

    @patch("src.py.functions.website_verification.verify_website_status")
    def test_returns_failed_items(self, mock_verify):
        mock_verify.side_effect = [
            {"status": "1", "status_code": 200, "error": None},
            {"status": "0", "status_code": None, "error": "Connection refused"},
        ]
        items = [
            {"Nome da Empresa": "OK", "URL": "https://ok.com", "Status da URL": "0"},
            {"Nome da Empresa": "Falha", "URL": "https://fail.com", "Status da URL": "0"},
        ]

        failed = verify_websites_concurrent(items, max_workers=1)
        assert len(failed) == 1
        assert failed[0]["Nome da Empresa"] == "Falha"

    @patch("src.py.functions.website_verification.verify_website_status")
    def test_all_succeed_returns_empty(self, mock_verify):
        mock_verify.return_value = {"status": "1", "status_code": 200, "error": None}
        items = [
            {"Nome da Empresa": "A", "URL": "https://a.com", "Status da URL": "0"},
        ]

        failed = verify_websites_concurrent(items, max_workers=1)
        assert failed == []

    @patch("src.py.functions.website_verification.verify_website_status")
    def test_all_fail_returns_all(self, mock_verify):
        mock_verify.return_value = {"status": "0", "status_code": None, "error": "timeout"}
        items = [
            {"Nome da Empresa": "A", "URL": "https://a.com", "Status da URL": "0"},
            {"Nome da Empresa": "B", "URL": "https://b.com", "Status da URL": "0"},
        ]

        failed = verify_websites_concurrent(items, max_workers=1)
        assert len(failed) == 2

    @patch("src.py.functions.website_verification.verify_website_status")
    def test_adds_error_to_failed_items(self, mock_verify):
        mock_verify.return_value = {"status": "0", "status_code": None, "error": "DNS error"}
        items = [
            {"Nome da Empresa": "A", "URL": "https://a.com", "Status da URL": "0"},
        ]

        failed = verify_websites_concurrent(items, max_workers=1)
        assert failed[0]["_error"] == "DNS error"

    @patch("src.py.functions.website_verification.verify_website_status")
    def test_empty_list(self, mock_verify):
        failed = verify_websites_concurrent([], max_workers=1)
        assert failed == []
        mock_verify.assert_not_called()
