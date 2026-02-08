import pytest

from src.py.functions.df_operations import clean_url, validate_url


class TestCleanUrl:
    def test_removes_trailing_slash(self):
        assert clean_url("https://example.com/") == "https://example.com"

    def test_removes_multiple_trailing_slashes(self):
        assert clean_url("https://example.com///") == "https://example.com"

    def test_removes_trailing_spaces(self):
        assert clean_url("https://example.com   ") == "https://example.com"

    def test_removes_leading_spaces(self):
        assert clean_url("   https://example.com") == "https://example.com"

    def test_removes_spaces_and_slashes(self):
        assert clean_url("  https://example.com/  ") == "https://example.com"

    def test_preserves_path(self):
        assert clean_url("https://example.com/jobs") == "https://example.com/jobs"

    def test_preserves_query_params(self):
        url = "https://example.com/search?q=dev"
        assert clean_url(url) == url

    def test_empty_string(self):
        assert clean_url("") == ""

    def test_url_without_trailing_slash(self):
        url = "https://example.com"
        assert clean_url(url) == url


class TestValidateUrl:
    def test_valid_https_url(self):
        assert validate_url("https://example.com") is True

    def test_valid_http_url(self):
        assert validate_url("http://example.com") is True

    def test_valid_url_with_path(self):
        assert validate_url("https://example.com/jobs/search") is True

    def test_invalid_no_scheme(self):
        assert validate_url("example.com") is False

    def test_invalid_ftp_scheme(self):
        assert validate_url("ftp://example.com") is False

    def test_invalid_empty(self):
        assert validate_url("") is False

    def test_invalid_just_scheme(self):
        assert validate_url("https://") is False

    def test_valid_with_trailing_slash(self):
        assert validate_url("https://example.com/") is True

    def test_valid_with_spaces(self):
        assert validate_url("  https://example.com  ") is True
