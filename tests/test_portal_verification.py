from unittest.mock import MagicMock, patch

from src.py.functions.portal_verification import (
    _gupy_has_jobs,
    _gupy_is_generic_portal,
    verify_portal_has_jobs,
)


class TestGupyGenericPortal:
    def test_generic_carreiras_redirect_detected(self):
        html = "<title>Página de Carreiras EuroChem</title>"
        final = "https://carreiras.gupy.io/"
        requested = "https://carreiras.gupy.io/fakecompany"
        assert _gupy_is_generic_portal(final, html, requested) is True

    def test_gupy_has_jobs_rejects_generic(self):
        html = "<title>Página de Carreiras EuroChem</title><script id=\"__NEXT_DATA__\">{}</script>"
        assert (
            _gupy_has_jobs(
                html,
                "https://carreiras.gupy.io/",
                "https://carreiras.gupy.io/fakecompany",
            )
            is False
        )

    @patch("src.py.functions.portal_verification._fetch_page")
    def test_verify_portal_delegates_gupy(self, mock_fetch):
        mock_fetch.return_value = (
            '<title>Empresa X</title><script id="__NEXT_DATA__">'
            '{"props":{"pageProps":{"jobs":[{"id":1}]}}}</script>',
            "https://empresa.gupy.io/",
        )
        session = MagicMock()
        assert verify_portal_has_jobs("https://empresa.gupy.io/", session) is True
