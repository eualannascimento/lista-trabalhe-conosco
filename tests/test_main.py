import csv
from unittest.mock import patch, MagicMock

import pytest

from main import (
    process_new_items,
    sort_and_deduplicate,
    save_results,
    print_failure_report,
)


class TestProcessNewItems:
    def test_adds_new_items(self, tmp_new_items_csv, tmp_csv):
        added, duplicates = process_new_items(tmp_new_items_csv, tmp_csv)
        assert added == 1
        assert duplicates == []

    def test_detects_duplicates(self, tmp_new_items_duplicate, tmp_csv):
        added, duplicates = process_new_items(tmp_new_items_duplicate, tmp_csv)
        assert added == 0
        assert len(duplicates) == 1

    def test_no_new_items(self, tmp_new_items_empty, tmp_csv):
        added, duplicates = process_new_items(tmp_new_items_empty, tmp_csv)
        assert added == 0
        assert duplicates == []

    def test_clears_new_items_after_processing(self, tmp_new_items_csv, tmp_csv):
        process_new_items(tmp_new_items_csv, tmp_csv)
        with open(tmp_new_items_csv, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            remaining = list(reader)
        assert remaining == []

    def test_preserves_existing_items(self, tmp_new_items_csv, tmp_csv):
        original_count = len(list(csv.DictReader(open(tmp_csv, encoding="utf-8"))))
        process_new_items(tmp_new_items_csv, tmp_csv)
        with open(tmp_csv, "r", encoding="utf-8") as f:
            new_count = len(list(csv.DictReader(f)))
        assert new_count == original_count + 1

    def test_new_item_gets_status_zero(self, tmp_new_items_csv, tmp_csv):
        process_new_items(tmp_new_items_csv, tmp_csv)
        with open(tmp_csv, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        new_item = [r for r in rows if r["Nome da Empresa"] == "Nova Empresa"]
        assert len(new_item) == 1
        assert new_item[0]["Status da URL"] == "0"


class TestSortAndDeduplicate:
    def test_sorts_alphabetically(self):
        items = [
            {"Nome da Empresa": "Zebra", "URL": "https://z.com"},
            {"Nome da Empresa": "Alpha", "URL": "https://a.com"},
            {"Nome da Empresa": "Beta", "URL": "https://b.com"},
        ]
        unique, _ = sort_and_deduplicate(items)
        names = [item["Nome da Empresa"] for item in unique]
        assert names == ["Alpha", "Beta", "Zebra"]

    def test_removes_duplicate_urls(self):
        items = [
            {"Nome da Empresa": "Empresa A", "URL": "https://same.com"},
            {"Nome da Empresa": "Empresa B", "URL": "https://same.com"},
            {"Nome da Empresa": "Empresa C", "URL": "https://different.com"},
        ]
        unique, dups = sort_and_deduplicate(items)
        assert len(unique) == 2
        assert len(dups) == 1

    def test_keeps_first_occurrence(self):
        items = [
            {"Nome da Empresa": "Alpha", "URL": "https://same.com"},
            {"Nome da Empresa": "Beta", "URL": "https://same.com"},
        ]
        unique, _ = sort_and_deduplicate(items)
        assert unique[0]["Nome da Empresa"] == "Alpha"

    def test_handles_accented_characters(self):
        items = [
            {"Nome da Empresa": "Çedilha", "URL": "https://c.com"},
            {"Nome da Empresa": "Alpha", "URL": "https://a.com"},
            {"Nome da Empresa": "Élan", "URL": "https://e.com"},
        ]
        unique, _ = sort_and_deduplicate(items)
        names = [item["Nome da Empresa"] for item in unique]
        assert names == ["Alpha", "Çedilha", "Élan"]

    def test_no_duplicates(self, sample_items):
        unique, dups = sort_and_deduplicate(sample_items)
        assert len(unique) == 3
        assert dups == []

    def test_empty_list(self):
        unique, dups = sort_and_deduplicate([])
        assert unique == []
        assert dups == []


class TestSaveResults:
    def test_saves_csv_and_readme(self, tmp_path, tmp_header_md):
        list_file = str(tmp_path / "output.csv")
        readme_file = str(tmp_path / "README.md")
        items = [
            {
                "Status da URL": "1",
                "Data de Entrada": "2025-01-01",
                "Nome da Empresa": "Test",
                "Segmento da Empresa": "Tech",
                "Plataforma": "Gupy",
                "URL": "https://test.com",
            }
        ]
        save_results(items, list_file, tmp_header_md, readme_file)

        with open(list_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        assert len(rows) == 1

        with open(readme_file, "r", encoding="utf-8") as f:
            content = f.read()
        assert "# Trabalhe Conosco" in content
        assert "[Test](https://test.com)" in content

    def test_removes_temporary_fields(self, tmp_path, tmp_header_md):
        list_file = str(tmp_path / "output.csv")
        readme_file = str(tmp_path / "README.md")
        items = [
            {
                "Status da URL": "1",
                "Data de Entrada": "2025-01-01",
                "Nome da Empresa": "Test",
                "Segmento da Empresa": "Tech",
                "Plataforma": "Gupy",
                "URL": "https://test.com",
                "Data do Status": "2025-01-01",
                "_error": "some error",
            }
        ]
        save_results(items, list_file, tmp_header_md, readme_file)
        assert "Data do Status" not in items[0]
        assert "_error" not in items[0]


class TestPrintFailureReport:
    def test_no_failures_prints_success(self, capsys):
        print_failure_report([])
        captured = capsys.readouterr()
        assert "Todas as URLs foram verificadas com sucesso" in captured.out

    def test_failures_print_count(self, capsys):
        failed = [
            {
                "Nome da Empresa": "Empresa Falha",
                "URL": "https://fail.com",
                "_error": "Connection refused",
            },
        ]
        print_failure_report(failed)
        captured = capsys.readouterr()
        assert "1 EMPRESA(S) COM FALHA" in captured.out
        assert "Empresa Falha" in captured.out
        assert "https://fail.com" in captured.out
        assert "Connection refused" in captured.out

    def test_multiple_failures_sorted(self, capsys):
        failed = [
            {"Nome da Empresa": "Zebra", "URL": "https://z.com", "_error": "timeout"},
            {"Nome da Empresa": "Alpha", "URL": "https://a.com", "_error": "DNS error"},
        ]
        print_failure_report(failed)
        captured = capsys.readouterr()
        lines = captured.out.split("\n")
        # Alpha deve vir antes de Zebra
        alpha_line = next(l for l in lines if "Alpha" in l)
        zebra_line = next(l for l in lines if "Zebra" in l)
        alpha_idx = lines.index(alpha_line)
        zebra_idx = lines.index(zebra_line)
        assert alpha_idx < zebra_idx

    def test_total_count_in_report(self, capsys):
        failed = [
            {"Nome da Empresa": "A", "URL": "https://a.com", "_error": "err"},
            {"Nome da Empresa": "B", "URL": "https://b.com", "_error": "err"},
            {"Nome da Empresa": "C", "URL": "https://c.com", "_error": "err"},
        ]
        print_failure_report(failed)
        captured = capsys.readouterr()
        assert "Total: 3 site(s)" in captured.out
