import pytest

from src.py.functions.md_operations import generate_markdown_table, load_header


class TestGenerateMarkdownTable:
    def test_generates_header(self):
        data = [{"Nome da Empresa": "Test", "URL": "https://test.com"}]
        result = generate_markdown_table(data)
        assert "| Nome da Empresa (+ Link do Trabalhe Conosco) |" in result
        assert "| --- |" in result

    def test_generates_links(self):
        data = [{"Nome da Empresa": "Empresa X", "URL": "https://x.com/jobs"}]
        result = generate_markdown_table(data)
        assert "| [Empresa X](https://x.com/jobs) |" in result

    def test_multiple_rows(self):
        data = [
            {"Nome da Empresa": "A", "URL": "https://a.com"},
            {"Nome da Empresa": "B", "URL": "https://b.com"},
            {"Nome da Empresa": "C", "URL": "https://c.com"},
        ]
        result = generate_markdown_table(data)
        lines = result.strip().split("\n")
        # header + separator + 3 data rows
        assert len(lines) == 5

    def test_empty_data(self):
        result = generate_markdown_table([])
        lines = result.strip().split("\n")
        # only header + separator
        assert len(lines) == 2

    def test_special_characters_in_name(self):
        data = [{"Nome da Empresa": "Empresa & Co.", "URL": "https://e.com"}]
        result = generate_markdown_table(data)
        assert "Empresa & Co." in result


class TestLoadHeader:
    def test_loads_content(self, tmp_header_md):
        content = load_header(tmp_header_md)
        assert "# Trabalhe Conosco" in content
        assert "Lista de empresas." in content

    def test_returns_string(self, tmp_header_md):
        content = load_header(tmp_header_md)
        assert isinstance(content, str)

    def test_preserves_newlines(self, tmp_path):
        file_path = tmp_path / "header.md"
        file_path.write_text("Line 1\nLine 2\nLine 3", encoding="utf-8")
        content = load_header(str(file_path))
        assert content.count("\n") == 2
