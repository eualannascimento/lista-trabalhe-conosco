import csv
import re

path = 'src/data/input/list.csv'
header = []
rows = []

# Improved granular mapping with word boundaries and context
mapping = [
    # 01 - Dados Subdivision (Specific companies)
    (r'\b(Alteryx|Cortex|Serasa|Experian|ClearSale|Boa Vista|Neoway|Dataloft|Konduto|Zoox|Birdie)\b', '01 - Dados: Analytics & IA'),
    
    # AI Technical (Strict word boundaries)
    (r'\b(Deepmind|OpenAI|Anthropic|Mistral|Deep Learning|Machine Learning|NLP|Vision|Computer Vision)\b', '01 - Dados: Inteligência Artificial'),
    
    # Specific Industry Refinement (Priority order matter)
    (r'\b(3R Petroleum|Eneva|Petrobras|Vibra|Ipiranga|Cosan|Ultrapar|Raízen|Petro Rio)\b', 'Energia/Petróleo'),
    (r'\b(99|iFood|Rappi|Daki|Box Delivery|Giross|Click Entregas|Eu Entrego|Uber|Loggi|Frete\.com)\b', 'Logística/Delivery'),
    (r'\b(Banco|Banestes|Banrisul|Caixa Econômica|Safra|BMG|Votorantim|BV|Inter|Semear|Topázio|Digio|B3|Nubank|BizCapital|C6 Bank|PagBank|PagSeguro|Stone|Ebanx|Acesso)\b', 'Finanças/Banco & Fintech'),
    (r'\b(Seguradora|Seguro|Porto Seguro|BB Seguridade|AIG|Allianz|Caixa Seguridade|SulAmérica|Bradesco Seguros|Liberty|Tokio Marine|Itaú Seguridade)\b', 'Finanças/Seguros'),
    (r'\b(Biolab|Blau|Cristália|Aché|Bayer|Roche|Novartis|Pfizer|Sanofi|AstraZeneca|Eurofarma)\b', 'Farmacêutica'),
    (r'\b(Supermercado|Atacadistas|Varejo|Carrefour|Zaffari|Condor|Angeloni|Akki|GPA|Big|Assaí|Roldão|Riachuelo|Renner|C&A|Lojas|Gazin|Fast Shop|Polishop|Leroy Merlin|Tok&Stok|Mobly|Vivara|Marisa|Hering|Reserva|Schutz)\b', 'Varejo'),
    (r'\b(Telecom|Internet|Brisanet|Algar|Vivo|Claro|Tim|Desktop|Unifique|Vero|Sumicity|Alloha)\b', 'Telecom'),
    (r'\b(Energia|Cemig|Celesc|CPFL|Equatorial|Energisa|EDP|Engie|Neoenergia|Eletrobras|Light|Enel|Copel)\b', 'Energia'),
    (r'\b(Saneamento|Cagece|Casan|Caesb|Sabesp|Copasa|Sanepar|Corsan|Saneago|Embasa)\b', 'Saneamento'),
    (r'\b(Agronegócio|Agro|BrasilAgro|AgroGalaxy|Amaggi|Cocal|Tereos|SLC Agrícola|Cocamar|Copacol|Coplana|Castrolanda)\b', 'Agronegócio'),
    (r'\b(Indústria|Facchini|Fras-le|Grendene|Dexco|Eternit|Gerdau|Vale|Suzano|Klabin|CBA|Randoncorp|Tupy|Marcopolo|WEG|Embraer|ArcelorMittal)\b', 'Indústria'),
    (r'\b(Universidade|Faculdade|Ânima|Yduqs|Cogna|Kroton|Estácio|UNIP|UNINOVE|Cruzeiro do Sul|Ser Educacional|Ser Educacional)\b', 'Educação'),
    (r'\b(Hospital|Dasa|Fleury|Hapvida|NotreDame|Unimed|Einstein|Sírio-Libanês|Rede D\'Or|Santa Casa)\b', 'Saúde'),
    (r'\b(Alimento|Bebida|Bacio di Latte|Bold Snacks|Caffeine Army|Coco Bambu|Fazenda Futuro|Frooty|Frimesa|Cheftime|Beleaf|M\. Dias Branco|Nestlé|Heineken|Ambev|Femsa|BRF|JBS|Marfrig|Minerva)\b', 'Alimentos e Bebidas'),
]

# We need to preserve original segments for those we can't classify
# Let's read the whole file and keep a copy for rollback if needed
# Actually, the user can just use git if I screw up, but I'll be careful.

updated_count = 0
with open(path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    header = reader.fieldnames
    for row in reader:
        name = row['Nome da Empresa']
        current_segment = row['Segmento da Empresa']
        
        # Reset if it was a false positive from round 1 (very likely if it has IA but isn't tech)
        # We'll re-apply the logic from scratch for current generic categories
        # generic = ['Estratégico', 'Tecnologia', 'Varejo', 'Indústria', 'Serviços', '01 - Dados: Inteligência Artificial']
        
        new_segment = current_segment
        for pattern, replacement in mapping:
            if re.search(pattern, name, re.IGNORECASE):
                new_segment = replacement
                break # First match wins
        
        # Specific fix for the "IA" bug: if it's currently AI but doesn't match AI patterns
        if current_segment == '01 - Dados: Inteligência Artificial' and not re.search(r'\b(Deepmind|OpenAI|Anthropic|Mistral|Deep Learning|Machine Learning|NLP|Vision|Computer Vision)\b', name, re.IGNORECASE):
             # Try to find another segment or return to a safe default
             found_new = False
             for pattern, replacement in mapping:
                 if re.search(pattern, name, re.IGNORECASE):
                     new_segment = replacement
                     found_new = True
                     break
             if not found_new:
                 new_segment = 'Estratégico' # Safe fallback for false positives
        
        if new_segment != current_segment:
            row['Segmento da Empresa'] = new_segment
            updated_count += 1
        rows.append(row)

with open(path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(rows)

print(f'Done! Corrected/Updated {updated_count} companies.')
