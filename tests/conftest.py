import csv
import os
import pytest


@pytest.fixture
def tmp_csv(tmp_path):
    """Cria um CSV temporário com dados de exemplo e retorna o caminho."""
    file_path = tmp_path / "list.csv"
    fieldnames = [
        "Status da URL",
        "Data de Entrada",
        "Nome da Empresa",
        "Segmento da Empresa",
        "Plataforma",
        "URL",
    ]
    rows = [
        {
            "Status da URL": "1",
            "Data de Entrada": "2025-01-01",
            "Nome da Empresa": "Empresa A",
            "Segmento da Empresa": "Tecnologia",
            "Plataforma": "Gupy",
            "URL": "https://empresaa.gupy.io",
        },
        {
            "Status da URL": "0",
            "Data de Entrada": "2025-01-02",
            "Nome da Empresa": "Empresa B",
            "Segmento da Empresa": "Saúde",
            "Plataforma": "Greenhouse",
            "URL": "https://boards.greenhouse.io/empresab",
        },
        {
            "Status da URL": "1",
            "Data de Entrada": "2025-01-03",
            "Nome da Empresa": "Çempresa C",
            "Segmento da Empresa": "Banco",
            "Plataforma": "Workday",
            "URL": "https://empresac.wd1.myworkdayjobs.com",
        },
    ]
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return str(file_path)


@pytest.fixture
def tmp_new_items_csv(tmp_path):
    """Cria um new_items.csv temporário."""
    file_path = tmp_path / "new_items.csv"
    fieldnames = ["Nome da Empresa", "Segmento da Empresa", "Plataforma", "URL"]
    rows = [
        {
            "Nome da Empresa": "Nova Empresa",
            "Segmento da Empresa": "Fintech",
            "Plataforma": "Lever",
            "URL": "https://jobs.lever.co/novaempresa",
        },
    ]
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return str(file_path)


@pytest.fixture
def tmp_new_items_empty(tmp_path):
    """Cria um new_items.csv vazio (só cabeçalho)."""
    file_path = tmp_path / "new_items.csv"
    fieldnames = ["Nome da Empresa", "Segmento da Empresa", "Plataforma", "URL"]
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
    return str(file_path)


@pytest.fixture
def tmp_new_items_duplicate(tmp_path, tmp_csv):
    """Cria um new_items.csv com um item que já existe em list.csv."""
    file_path = tmp_path / "new_items_dup.csv"
    fieldnames = ["Nome da Empresa", "Segmento da Empresa", "Plataforma", "URL"]
    rows = [
        {
            "Nome da Empresa": "Empresa A Duplicada",
            "Segmento da Empresa": "Tecnologia",
            "Plataforma": "Gupy",
            "URL": "https://empresaa.gupy.io",
        },
    ]
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return str(file_path)


@pytest.fixture
def tmp_header_md(tmp_path):
    """Cria um header.md temporário."""
    file_path = tmp_path / "header.md"
    file_path.write_text("# Trabalhe Conosco\nLista de empresas.", encoding="utf-8")
    return str(file_path)


@pytest.fixture
def sample_items():
    """Retorna uma lista de itens de exemplo para testes."""
    return [
        {
            "Status da URL": "1",
            "Data de Entrada": "2025-01-01",
            "Nome da Empresa": "Zebra Corp",
            "Segmento da Empresa": "Tecnologia",
            "Plataforma": "Gupy",
            "URL": "https://zebra.gupy.io",
        },
        {
            "Status da URL": "1",
            "Data de Entrada": "2025-01-02",
            "Nome da Empresa": "Alpha Inc",
            "Segmento da Empresa": "Saúde",
            "Plataforma": "Greenhouse",
            "URL": "https://boards.greenhouse.io/alpha",
        },
        {
            "Status da URL": "0",
            "Data de Entrada": "2025-01-03",
            "Nome da Empresa": "Beta SA",
            "Segmento da Empresa": "Banco",
            "Plataforma": "Workday",
            "URL": "https://beta.wd1.myworkdayjobs.com",
        },
    ]
