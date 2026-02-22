import csv
import re

path = 'src/data/input/list.csv'
header = []
rows = []

# Granular mapping for "01 - Dados" and industry refinement
mapping = {
    # 01 - Dados Subdivision
    r'Alteryx|Cortex|Serasa|Experian|ClearSale|Boa Vista|Neoway|Dataloft|Konduto|Zoox|Birdie': '01 - Dados: Analytics & IA',
    r'Deep|Machine Learning|IA|Artificial Intelligence|NLP|Vision|Computer Vision': '01 - Dados: Inteligência Artificial',
    
    # Industry Refinement
    r'3R Petroleum|Eneva|Petrobras|Vibra|Ipiranga|Cosan|Ultrapar|Raízen|Petro Rio|Petrobras': 'Energia/Petróleo',
    r'99|iFood|Rappi|Daki|Box Delivery|Giross|Click Entregas|Eu Entrego|Uber|Loggi|Frete.com': 'Logística/Delivery',
    r'Alimentos|Bebidas|Bacio di Latte|Bold Snacks|Caffeine Army|Coco Bambu|Fazenda Futuro|Frooty|Frimesa|Cheftime|Beleaf|Bold|M. Dias Branco|Nestlé|Heineken|Ambev': 'Alimentos e Bebidas',
    r'Supermercado|Atacadistas|Varejo|Carrefour|Zaffari|Condor|Angeloni|Akki|Pão de Açúcar|Extra|GPA|Big|Assaí|Roldão|Riachuelo|Renner|C&A|Lojas|Gazin|Fast Shop|Polishop|Leroy Merlin|Tok&Stok': 'Varejo',
    r'Agronegócio|Agro|BrasilAgro|AgroGalaxy|Amaggi|Cocal|Tereos|SLC Agrícola|Cocamar|Copacol|Copacol|Coplana|Castrolanda': 'Agronegócio',
    r'Indústria|Facchini|Fras-le|Grendene|Dexco|Eternit|Gerdau|Vale|Suzano|Klabin|CBA|Amaggi|Randoncorp|Tupy|Marcopolo|WEG|Embraer|ArcelorMittal': 'Indústria',
    r'Energia|Saneamento|Copel|Embasa|Cemig|Celesc|CPFL|Equatorial|Energisa|EDP|Engie|Neoenergia|Eletrobras|Light|Enel|Cagece|Casan|Caesb|Sabesp|Copasa|Sanepar|Saneago': 'Energia e Utilidades',
    r'Banco|Finanças|Fintech|Nubank|Inter|BMG|Votorantim|BV|Safra|Digio|Semear|Topázio|Semear|B3|BizCapital|Foxbit|Geru|C6 Bank|PagBank|PagSeguro|Stone|Ebanx|Acesso': 'Finanças/Banco & Fintech',
    r'Seguradora|Seguro|Porto Seguro|BB Seguridade|AIG|Allianz|Caixa Seguridade|SulAmérica|Bradesco Seguros|Liberty|Tokio Marine|Itaú Seguridade': 'Finanças/Seguros',
    r'Telecom|Internet|Brisanet|Algar|Vivo|Claro|Tim|Desktop|Unifique|Vero|Sumicity|Alloha|Unifique': 'Telecom',
}

def get_better_segment(name, current_segment):
    # If it's already a granular data tag, don't overwrite with generic industry
    if current_segment.startswith('01 - Dados'):
        return current_segment
        
    for pattern, new_segment in mapping.items():
        if re.search(pattern, name, re.IGNORECASE):
            return new_segment
    return current_segment

updated_count = 0
with open(path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    header = reader.fieldnames
    for row in reader:
        original = row['Segmento da Empresa']
        name = row['Nome da Empresa']
        new_s = get_better_segment(name, original)
        if new_s != original:
            row['Segmento da Empresa'] = new_s
            updated_count += 1
        rows.append(row)

with open(path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(rows)

print(f'Done! Updated {updated_count} companies.')
