# Critérios: empresa grande no Brasil (lista trabalhe-conosco)

Este documento define o nível de empresa aceito ao expandir [`src/data/input/list.csv`](../src/data/input/list.csv).

## Mesmo meio (obrigatório)

Portal de **carreiras / trabalhe conosco** em ATS ou site corporativo de RH:

| Prioridade | Plataformas |
|------------|-------------|
| 1 | Gupy, InHire, InfoJobs/PandaPe, Sólides, Recrut.ai |
| 2 | Greenhouse, Workday, Lever, SAP SuccessFactors, CSOD, Eightfold, Workable |
| 3 | Site da Empresa, Manual (estatais, utilities) |

Não entram: perfil LinkedIn genérico, página de contato, domínio InHire sem marca (ex.: `analytics.inhire.com.br`).

## Score de elegibilidade (mínimo 4 para incluir)

| Sinal | Pontos |
|-------|--------|
| Listada B3 (ou BDR de grupo listado) | +3 |
| Faturamento estimado > R$ 1 bi/ano | +2 |
| > 2.000 funcionários no Brasil | +2 |
| Top 3 nacional do setor (seed curada) | +2 |
| Multinacional Fortune 500 com portal BR | +2 |
| Consultoria pequena / portal genérico | -3 |

Configuração em [`data/seeds/scoring.yaml`](../data/seeds/scoring.yaml).

## Verificação de URL

1. HTTP acessível (`verify_website_status`).
2. **Verificação forte:** conteúdo indica portal de vagas (`verify_portal_has_jobs`).

Só entra na lista com as duas aprovadas; caso contrário → `artifacts/pending_companies.csv`.

## Exemplos

**Incluir:** Vale, Itaú, Ambev, Localiza, Rede D'Or, WEG, Nubank, Carrefour Brasil.

**Excluir ao escalar:** consultorias com nome genérico + portal Gupy sem vagas; slugs `carreiras.gupy.io/{x}` que retornam página vazia.
