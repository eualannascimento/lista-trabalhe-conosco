import csv
from pathlib import Path

import pytest

from scripts.archive_companies import ARCHIVE_FIELDS, archive_by_names, load_archived
from scripts.url_repair import slugify_name, is_reachable_url


class TestUrlRepair:
    def test_slugify_name(self):
        assert slugify_name("Itaú S.A.") == "itausa"

    def test_generic_gupy_portal_not_reachable(self):
        assert is_reachable_url("https://carreiras.gupy.io/livelo") is False


class TestArchiveCompanies:
    def test_archive_by_names(self, tmp_path, monkeypatch):
        list_csv = tmp_path / "list.csv"
        archived_csv = tmp_path / "archived.csv"
        list_csv.write_text(
            "Status da URL,Data de Entrada,Nome da Empresa,Segmento da Empresa,Plataforma,URL,Data de Publicação\n"
            "0,2024-01-01,Empresa X,Seg,Vagas,https://x.com,\n"
            "1,2024-01-01,Empresa Y,Seg,Vagas,https://y.com,\n",
            encoding="utf-8",
        )
        archived_csv.write_text(
            ",".join(ARCHIVE_FIELDS) + "\n",
            encoding="utf-8",
        )

        import scripts.archive_companies as arch

        monkeypatch.setattr(arch, "LIST_CSV", list_csv)
        monkeypatch.setattr(arch, "ARCHIVED_CSV", archived_csv)

        n = archive_by_names(["Empresa X"], "teste")
        assert n == 1

        remaining = list(csv.DictReader(open(list_csv, encoding="utf-8")))
        assert len(remaining) == 1
        assert remaining[0]["Nome da Empresa"] == "Empresa Y"

        archived = load_archived()
        assert len(archived) == 1
        assert archived[0]["Nome da Empresa"] == "Empresa X"
        assert archived[0]["Motivo"] == "teste"
