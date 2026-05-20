"""Mapa de segmentos detalhados para 12 categorias macro."""

from unidecode import unidecode

MACRO_SEGMENTS = (
    "Financeiro",
    "Tecnologia",
    "Varejo e Consumo",
    "Saúde",
    "Indústria",
    "Energia e Utilities",
    "Logística e Mobilidade",
    "Construção e Imóveis",
    "Educação",
    "Agro e Alimentos",
    "Mídia e Entretenimento",
    "Serviços e Outros",
)

EXACT_MAP = {
    "Estratégico": "Serviços e Outros",
    "Tecnologia": "Tecnologia",
    "Finanças/Banco & Fintech": "Financeiro",
    "Varejo": "Varejo e Consumo",
    "Saúde": "Saúde",
    "Alimentos e Bebidas": "Agro e Alimentos",
    "Indústria": "Indústria",
    "Fintech": "Financeiro",
    "Logística": "Logística e Mobilidade",
    "Educação": "Educação",
    "Automotivo": "Indústria",
    "Consultoria": "Serviços e Outros",
    "Energia": "Energia e Utilities",
    "Construção": "Construção e Imóveis",
    "Agronegócio": "Agro e Alimentos",
    "Financeiro": "Financeiro",
    "Farmacêutica": "Saúde",
    "Logística/Delivery": "Logística e Mobilidade",
    "Games": "Mídia e Entretenimento",
    "Telecom": "Energia e Utilities",
    "Aviação": "Logística e Mobilidade",
    "Banco": "Financeiro",
    "Mídia": "Mídia e Entretenimento",
    "Saneamento": "Energia e Utilities",
    "Moda": "Varejo e Consumo",
    "Finanças/Seguros": "Financeiro",
    "Serviços": "Serviços e Outros",
    "Energia/Petróleo": "Energia e Utilities",
    "Alimentação": "Agro e Alimentos",
    "Alimentos": "Agro e Alimentos",
    "Hospitalidade": "Mídia e Entretenimento",
    "Entretenimento": "Mídia e Entretenimento",
    "Benefícios": "Financeiro",
    "Finanças": "Financeiro",
    "Infraestrutura": "Construção e Imóveis",
    "Turismo": "Mídia e Entretenimento",
    "Soluções de Pagamento": "Financeiro",
    "Jogos": "Mídia e Entretenimento",
    "Cosméticos": "Varejo e Consumo",
    "Educacional": "Educação",
    "Cibersegurança": "Tecnologia",
    "01 - Dados: Analytics & IA": "Tecnologia",
    "E-commerce": "Varejo e Consumo",
    "Eletrônicos": "Varejo e Consumo",
    "Bancário": "Financeiro",
    "Bens de Consumo": "Varejo e Consumo",
    "Mobilidade": "Logística e Mobilidade",
    "Esportes": "Mídia e Entretenimento",
    "Televisão": "Mídia e Entretenimento",
    "Seguros": "Financeiro",
    "Siderurgia": "Indústria",
    "HRTech": "Tecnologia",
    "Healthtech": "Tecnologia",
    "Eletrodomesticos": "Varejo e Consumo",
    "Eletrodomésticos": "Varejo e Consumo",
    "Transporte": "Logística e Mobilidade",
    "EdTech": "Tecnologia",
    "HR Tech": "Tecnologia",
    "Redes Sociais": "Tecnologia",
    "Cooperativa": "Financeiro",
    "Entidade Financeira": "Financeiro",
    "Restaurante": "Agro e Alimentos",
    "Bebidas": "Agro e Alimentos",
    "Cultura": "Mídia e Entretenimento",
    "Imobiliário": "Construção e Imóveis",
    "Gestão de Relacionamentos": "Serviços e Outros",
    "Seguradora": "Financeiro",
    "Locação": "Logística e Mobilidade",
    "Marketplace": "Varejo e Consumo",
    "Energy": "Energia e Utilities",
    "Recompensas": "Financeiro",
    "Birô de Crédito": "Financeiro",
    "Social": "Serviços e Outros",
    "SaaS": "Tecnologia",
    "Pet Shop": "Varejo e Consumo",
    "Pet": "Varejo e Consumo",
    "Aluguel de Veículos": "Logística e Mobilidade",
    "Papelaria": "Varejo e Consumo",
    "Shopping": "Varejo e Consumo",
    "Associação": "Serviços e Outros",
    "01 - Dados: Inteligência Artificial": "Tecnologia",
    "Embalagens": "Indústria",
    "Comunicação": "Mídia e Entretenimento",
    "Química": "Indústria",
    "Setor Público": "Serviços e Outros",
    "Supermercado": "Varejo e Consumo",
    "Esporte": "Mídia e Entretenimento",
    "RH Tech": "Tecnologia",
    "Ensino": "Educação",
    "Viagens": "Mídia e Entretenimento",
    "Trade Marketing": "Serviços e Outros",
    "Produtos de Consumo": "Varejo e Consumo",
    "TI": "Tecnologia",
    "Comércio": "Varejo e Consumo",
    "Registro de Imóveis Eletrônico": "Serviços e Outros",
    "Software": "Tecnologia",
    "Imóveis": "Construção e Imóveis",
    "Proptech": "Tecnologia",
    "Comércio Eletrônico": "Varejo e Consumo",
    "ID Tech": "Tecnologia",
    "Espaços de Trabalho": "Serviços e Outros",
    "Delivery": "Logística e Mobilidade",
}

NAME_KEYWORDS = [
    (("banco", "bank", "fintech", "seguro", "credito", "credit", "pagamento", "finance"), "Financeiro"),
    (("hospital", "saude", "saúde", "farmaceut", "farmac", "odont", "clinica", "laboratorio"), "Saúde"),
    (("universidade", "educacao", "educação", "faculdade", "escola", "senac", "senai", "fiap"), "Educação"),
    (("logistica", "logística", "transporte", "entrega", "delivery", "aviacao", "aviação", "aereo"), "Logística e Mobilidade"),
    (("energia", "eletrica", "elétrica", "petro", "gas ", "gás", "saneamento", "telecom", "vivo", "tim ", "claro"), "Energia e Utilities"),
    (("constru", "imob", "incorpor", "engenharia civil"), "Construção e Imóveis"),
    (("agro", "alimento", "bebida", "cafe", "café", "frigor", "supermerc", "atacad"), "Agro e Alimentos"),
    (("varejo", "loja", "moda", "cosmet"), "Varejo e Consumo"),
    (("tech", "software", "digital", "data", "cloud", "cyber"), "Tecnologia"),
    (("industria", "indústria", "metal", "sider", "automot", "veicul"), "Indústria"),
    (("game", "midia", "mídia", "tv ", "cinema", "entreten"), "Mídia e Entretenimento"),
]


def _normalize(text: str) -> str:
    return unidecode((text or "").lower())


def macro_from_name(name: str) -> str | None:
    n = _normalize(name)
    for keywords, macro in NAME_KEYWORDS:
        if any(k in n for k in keywords):
            return macro
    return None


def to_macro(segment: str, company_name: str = "") -> str:
    if segment in EXACT_MAP:
        macro = EXACT_MAP[segment]
        if macro == "Serviços e Outros" and segment == "Estratégico":
            guessed = macro_from_name(company_name)
            if guessed:
                return guessed
        return macro
    guessed = macro_from_name(company_name)
    return guessed or "Serviços e Outros"
