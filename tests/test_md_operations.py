import pytest

from src.py.functions.md_operations import generate_markdown_table, load_header


class TestGenerateMarkdownTable:
    def test_generates_header(self):
        data = [{"Nome da Empresa": "Test", "URL": "https://test.com", "Status da URL": "1"}]
        result = generate_markdown_table(data)
        assert "| Nome da Empresa (+ Link do Trabalhe Conosco) |" in result
        assert "| --- |" in result

    def test_generates_links(self):
        data = [{"Nome da Empresa": "Empresa X", "URL": "https://x.com/jobs", "Status da URL": "1"}]
        result = generate_markdown_table(data)
        assert "| [Empresa X](https://x.com/jobs) |" in result

    def test_multiple_rows(self):
        data = [
            {"Nome da Empresa": "A", "URL": "https://a.com", "Status da URL": "1"},
            {"Nome da Empresa": "B", "URL": "https://b.com", "Status da URL": "1"},
            {"Nome da Empresa": "C", "URL": "https://c.com", "Status da URL": "1"},
        ]
        result = generate_markdown_table(data)
        lines = result.strip().split("\n")
        assert len(lines) == 5

    def test_empty_data(self):
        result = generate_markdown_table([])
        lines = result.strip().split("\n")
        assert len(lines) == 2

    def test_special_characters_in_name(self):
        data = [{"Nome da Empresa": "Empresa & Co.", "URL": "https://e.com", "Status da URL": "1"}]
        result = generate_markdown_table(data)
        assert "Empresa & Co." in result

    def test_active_only_excludes_status_zero(self):
        data = [
            {
                "Nome da Empresa": "Ativa",
                "URL": "https://ativa.com",
                "Segmento da Empresa": "Tech",
                "Data de Publicação": "",
                "Status da URL": "1",
            },
            {
                "Nome da Empresa": "Inativa",
                "URL": "https://inativa.com",
                "Segmento da Empresa": "Tech",
                "Data de Publicação": "",
                "Status da URL": "0",
            },
        ]
        md = generate_markdown_table(data, active_only=True)
        assert "Ativa" in md
        assert "Inativa" not in md

    def test_active_only_false_includes_all(self):
        data = [
            {
                "Nome da Empresa": "Inativa",
                "URL": "https://inativa.com",
                "Segmento da Empresa": "Tech",
                "Data de Publicação": "",
                "Status da URL": "0",
            },
        ]
        md = generate_markdown_table(data, active_only=False)
        assert "Inativa" in md
