import csv
import pytest

from src.py.functions.file_operations import read_csv, read_and_filter_csv, save_sorted_csv


class TestReadCsv:
    def test_reads_all_rows(self, tmp_csv):
        data = read_csv(tmp_csv)
        assert len(data) == 3

    def test_returns_list_of_dicts(self, tmp_csv):
        data = read_csv(tmp_csv)
        assert isinstance(data, list)
        assert all(isinstance(row, dict) for row in data)

    def test_preserves_field_values(self, tmp_csv):
        data = read_csv(tmp_csv)
        assert data[0]["Nome da Empresa"] == "Empresa A"
        assert data[0]["URL"] == "https://empresaa.gupy.io"

    def test_reads_all_fields(self, tmp_csv):
        data = read_csv(tmp_csv)
        expected_fields = {
            "Status da URL",
            "Data de Entrada",
            "Nome da Empresa",
            "Segmento da Empresa",
            "Plataforma",
            "URL",
        }
        assert set(data[0].keys()) == expected_fields

    def test_empty_csv(self, tmp_path):
        file_path = tmp_path / "empty.csv"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("Nome da Empresa,URL\n")
        data = read_csv(str(file_path))
        assert data == []


class TestReadAndFilterCsv:
    def test_cleans_urls(self, tmp_path):
        file_path = tmp_path / "dirty.csv"
        fieldnames = ["Status da URL", "Data de Entrada", "Nome da Empresa",
                       "Segmento da Empresa", "Plataforma", "URL"]
        rows = [{
            "Status da URL": "1",
            "Data de Entrada": "2025-01-01",
            "Nome da Empresa": "Test",
            "Segmento da Empresa": "Tech",
            "Plataforma": "Gupy",
            "URL": "https://example.com/ ",
        }]
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        data = read_and_filter_csv(str(file_path))
        assert data[0]["URL"] == "https://example.com"

    def test_returns_correct_count(self, tmp_csv):
        data = read_and_filter_csv(tmp_csv)
        assert len(data) == 3


class TestSaveSortedCsv:
    def test_saves_data(self, tmp_path):
        file_path = str(tmp_path / "output.csv")
        fieldnames = ["Nome", "URL"]
        data = [
            {"Nome": "A", "URL": "https://a.com"},
            {"Nome": "B", "URL": "https://b.com"},
        ]
        save_sorted_csv(file_path, data, fieldnames)

        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            result = list(reader)
        assert len(result) == 2
        assert result[0]["Nome"] == "A"

    def test_writes_header(self, tmp_path):
        file_path = str(tmp_path / "output.csv")
        fieldnames = ["Col1", "Col2"]
        save_sorted_csv(file_path, [], fieldnames)

        with open(file_path, "r", encoding="utf-8") as f:
            header = f.readline().strip()
        assert header == "Col1,Col2"

    def test_ignores_extra_fields(self, tmp_path):
        file_path = str(tmp_path / "output.csv")
        fieldnames = ["Nome"]
        data = [{"Nome": "X", "Extra": "ignorar"}]
        save_sorted_csv(file_path, data, fieldnames)

        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            result = list(reader)
        assert "Extra" not in result[0]

    def test_overwrites_existing_file(self, tmp_path):
        file_path = str(tmp_path / "output.csv")
        fieldnames = ["Nome"]
        save_sorted_csv(file_path, [{"Nome": "Antigo"}], fieldnames)
        save_sorted_csv(file_path, [{"Nome": "Novo"}], fieldnames)

        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            result = list(reader)
        assert len(result) == 1
        assert result[0]["Nome"] == "Novo"
