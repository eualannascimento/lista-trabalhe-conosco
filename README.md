## 📚 Introdução
O objetivo deste repositório é facilitar o acesso e a busca por oportunidades de trabalho em diferentes empresas, centralizando as plataformas em um só lugar.  
Sinta-se à vontade para contribuir adicionando ou atualizando a lista de empresas.  
Este repositório contém uma lista com: 
- Data de Entrada (quando entrou na lista);
- Nome da Empresa;
- Segmento da Empresa (12 categorias macro);
- Plataforma para processo seletivo;
- Link para acesso ao site;
- Status da URL (se o link está ativo ou não, atualizado pelo CI).
<br><br>  
## 🔧 Processo
O processo de atualização do README.md para acesso rápido é automatizado por meio do GitHub Actions.  
- O fluxo de trabalho `verify-and-update-list.yml` roda em push na branch `main` e semanalmente.  
- Ele executa `main.py`, que lê `src/data/input/list.csv` e `src/data/input/header.md`, verifica URLs em paralelo, ordena por nome e gera o `README.md`.
<br><br>
## 🤝 Como contribuir
1. Faça um fork do repositório do projeto;
2. Edite `src/data/input/new_items.csv` (ou `src/data/input/list.csv`) com suas contribuições;
3. Abra um PR — o CI valida os links e atualiza o README.
4. Faça o commit e o push para o seu repositório forkado.
5. Abra um pull request (PR) para o repositório original do projeto, especificando que deseja adicionar ou editar empresas.
6. Aguarde a revisão do PR (possíveis solicitações de alteração) e a eventual aprovação e merge.
<br><br>
## 🏢 Acesso rápido
Para obter todas as informações disponíveis, baixe `src/data/input/list.csv`.  
Essa tabela contém somente o nome da empresa com link para o site, visando facilitar o uso via mobile.
<br>

| Nome da Empresa (+ Link do Trabalhe Conosco) | Segmento | Plataforma |
| --- | --- | --- |
| [1Doc](https://1doc.gupy.io) | Saúde | Gupy |
| [2comconsulting](https://2comconsulting.gupy.io) | Serviços e Outros | Gupy |
| [3coracoes](https://3coracoes.gupy.io) | Serviços e Outros | Gupy |
| [3corptechnology](https://3corptechnology.gupy.io) | Tecnologia | Gupy |
| [3cservices](https://3cservices.gupy.io) | Serviços e Outros | Gupy |
| [3M](https://3m.wd1.myworkdayjobs.com/Search) | Indústria | Workday |
| [3R Petroleum](https://3rpetroleum.gupy.io) | Energia e Utilities | Gupy |
| [3tentos](https://3tentos.gupy.io) | Serviços e Outros | Gupy |
| [4mk](https://4mk.gupy.io) | Tecnologia | Gupy |
| [77sol](https://77sol.gupy.io) | Tecnologia | Gupy |
| [99 (99Entrega)](https://99app.com/carreiras) | Logística e Mobilidade | Vagas |
| [A3consultoria](https://a3consultoria.gupy.io) | Serviços e Outros | Gupy |
| [Aacd](https://aacd.gupy.io) | Saúde | Gupy |
| [AB InBev](https://job-boards.greenhouse.io/abinbev) | Serviços e Outros | Greenhouse |
| [Abaco](https://abaco.gupy.io) | Serviços e Outros | Gupy |
| [Abakids](https://abakids.gupy.io) | Educação | Gupy |
| [Accenture](https://www.accenture.com/br-pt/careers) | Serviços e Outros | Workday |
| [Accona](https://www.acciona.com.br/trabalhe-conosco) | Serviços e Outros | Site da Empresa |
| [Accor](https://careers.accor.com) | Serviços e Outros | Site da Empresa |
| [Acer](https://career10.successfactors.com/career?company=acerincorp) | Serviços e Outros | SAP SuccessFactors |
| [Aché](https://vagasache.gupy.io) | Saúde | Gupy |
| [Activision Blizzard](https://careers.activisionblizzard.com) | Serviços e Outros | Site da Empresa |
| [Adidas Brasil](https://adidas.gupy.io) | Serviços e Outros | Gupy |
| [Adobe](https://adobe.wd5.myworkdayjobs.com/external_experienced) | Tecnologia | Workday |
| [ADP](https://jobs.adp.com) | Serviços e Outros | Site da Empresa |
| [Aegea](https://aegea.gupy.io) | Serviços e Outros | Gupy |
| [AES Brasil](https://aes.wd1.myworkdayjobs.com/Careers) | Serviços e Outros | Vagas |
| [Aevo](https://aevo.gupy.io) | Tecnologia | Gupy |
| [Afya Educacional](https://afya.gupy.io) | Educação | Gupy |
| [Agibank](https://job-boards.greenhouse.io/agibank) | Financeiro | Greenhouse |
| [Agilize](https://boards.greenhouse.io/agilize) | Financeiro | Greenhouse |
| [Agoda](https://careersatagoda.com/vacancies/?search&teams&locations) | Tecnologia | Plataforma Interna |
| [Agrale](https://www.agrale.com.br/pt/trabalhe-conosco) | Serviços e Outros | Vagas |
| [Agrária](https://agraria.gupy.io) | Serviços e Outros | Gupy |
| [AgroGalaxy](https://agrogalaxy.gupy.io) | Agro e Alimentos | Gupy |
| [Ailos Sistema](https://ailos.gupy.io) | Financeiro | Gupy |
| [Aiqfome](https://aiqfome.gupy.io) | Serviços e Outros | Gupy |
| [Air France-KLM](https://recrutement.airfrance.com) | Serviços e Outros | Site da Empresa |
| [Airbnb](https://boards.greenhouse.io/airbnb) | Serviços e Outros | Greenhouse |
| [Albert Einstein](https://www.einstein.br/carreiras) | Saúde | Manual |
| [Alelo](https://alelo.inhire.app/vagas) | Financeiro | InHire |
| [Algar Tech Br](https://algar.gupy.io) | Tecnologia | Gupy |
| [Alibaba](https://talent.alibaba.com) | Serviços e Outros | Site da Empresa |
| [Alice](https://alice.inhire.app/vagas) | Tecnologia | InHire |
| [Alliar](https://alliar.gupy.io) | Serviços e Outros | Gupy |
| [Allied](https://allied.pandape.infojobs.com.br) | Serviços e Outros | Vagas |
| [Alloha Fibra](https://allohafibra.gupy.io) | Serviços e Outros | Gupy |
| [Allos](https://carreiras.gupy.io/allos) | Serviços e Outros | Gupy |
| [Alpargatas](https://alpargatas.gupy.io) | Indústria | Gupy |
| [Alteryx](https://www.alteryx.com/careers) | Tecnologia | Manual |
| [Alupar](https://alupar.gupy.io) | Serviços e Outros | Gupy |
| [Alura](https://alun.inhire.app/alura/vagas) | Educação | InHire |
| [Amaggi](https://carreiras.gupy.io/amaggi) | Serviços e Outros | Gupy |
| [Amazon](https://www.amazon.jobs) | Tecnologia | Site da Empresa |
| [Ambev](https://ambev.gupy.io) | Serviços e Outros | Gupy |
| [Ambev Tech](https://ambevtech.gupy.io) | Tecnologia | Gupy |
| [Ambipar](https://ambipar.gupy.io) | Serviços e Outros | Gupy |
| [Amcham Brasil](https://amcham.gupy.io) | Serviços e Outros | Gupy |
| [Ame Digital](https://ame.gupy.io) | Tecnologia | Gupy |
| [American Airlines](https://jobs.aa.com) | Serviços e Outros | Manual |
| [American Express](https://aexp.eightfold.ai/careers) | Financeiro | Eightfold |
| [Americanas S.A.](https://americanas.gupy.io) | Serviços e Outros | Gupy |
| [Amex](https://www.americanexpress.com/en-us/careers) | Financeiro | Site da Empresa |
| [Amil](https://career19.sapsf.com/careers?company=amilassist) | Saúde | SAP SuccessFactors |
| [Analytics](https://carreiras.gupy.io/analytics) | Tecnologia | Gupy |
| [Analytics-ss](https://analytics-ss.inhire.com.br) | Tecnologia | InHire |
| [ANBIMA](https://anbima.gupy.io) | Financeiro | Gupy |
| [Andorinha Supermercados](https://andorinha.gupy.io) | Agro e Alimentos | Gupy |
| [Andrade Gutierrez](https://andradegutierrez.gupy.io) | Serviços e Outros | Gupy |
| [Ânima Educação](https://anima.gupy.io) | Educação | Gupy |
| [Animale Moda Br](https://animale.gupy.io) | Varejo e Consumo | Gupy |
| [Anthropic](https://boards.greenhouse.io/anthropic) | Tecnologia | Greenhouse |
| [Apple](https://www.apple.com/careers/br) | Tecnologia | Site da Empresa |
| [Apptite](https://apptite.gupy.io) | Serviços e Outros | Gupy |
| [Aramis](https://aramis.gupy.io) | Serviços e Outros | Gupy |
| [ArcelorMittal Tuper Brasil](https://tuper.gupy.io) | Indústria | Gupy |
| [Arco Educação](https://boards.greenhouse.io/arcoeducacao) | Educação | Greenhouse |
| [Arcos Dorados (McDonald s)](https://trabalheconosconamc.infojobs.com.br) | Serviços e Outros | Infojobs |
| [Arezzo&Co](https://azzas2154.gupy.io) | Serviços e Outros | Gupy |
| [Armac](https://armac.gupy.io) | Serviços e Outros | Gupy |
| [Arteris](https://arteris.gupy.io) | Serviços e Outros | Gupy |
| [Asaas](https://asaas.gupy.io) | Financeiro | Gupy |
| [Assaí Atacadista](https://assai.gupy.io) | Agro e Alimentos | Gupy |
| [AstraZeneca](https://astrazeneca.wd3.myworkdayjobs.com/Careers) | Saúde | Workday |
| [Asus](https://www.asus.com/about-asus/careers) | Tecnologia | Site da Empresa |
| [Atacadão](https://carreiras.gupy.io/atacadao) | Agro e Alimentos | Gupy |
| [Atlantica Hospitality](https://atlantica.gupy.io) | Saúde | Gupy |
| [Atlassian](https://www.atlassian.com/company/careers) | Serviços e Outros | Site da Empresa |
| [Auren Energia](https://aurenenergia.gupy.io) | Energia e Utilities | Gupy |
| [AuroraCoop (Aurora Alimentos)](https://auroracoop.gupy.io) | Agro e Alimentos | Gupy |
| [Autodesk](https://www.autodesk.com/careers) | Tecnologia | Manual |
| [Automob](https://automob.gupy.io) | Indústria | Gupy |
| [Avanade](https://www.avanade.com/pt-br/career/search-jobs) | Tecnologia | Plataforma Interna |
| [Azos](https://azos.inhire.app/vagas) | Financeiro | InHire |
| [Aztec](https://job-boards.eu.greenhouse.io/aztec) | Tecnologia | Greenhouse |
| [Azul](https://voeazul.gupy.io) | Serviços e Outros | Gupy |
| [Azul Linhas Aéreas](https://azul.gupy.io) | Serviços e Outros | Gupy |
| [B3](https://b3.gupy.io) | Financeiro | Gupy |
| [Bacio di Latte](https://baciodilatte.com.br/carreiras) | Serviços e Outros | Vagas |
| [Bahema Educação](https://bahemaeducacao.com.br/trabalhe-conosco) | Educação | Vagas |
| [Ball](https://jobs.ball.com/corp_packaging/search) | Indústria | Plataforma Interna |
| [Banco ABC](https://abcbrasil.gupy.io) | Financeiro | Gupy |
| [Banco ABC Brasil](https://bancoabc.gupy.io) | Financeiro | Gupy |
| [Banco BMG](https://bancobmg.gupy.io) | Financeiro | Gupy |
| [Banco Bradesco](https://bradesco.csod.com/ux/ats/careersite/1/home?c=bradesco) | Financeiro | CSOD |
| [Banco BV](https://jobs.lever.co/bv) | Financeiro | Lever |
| [Banco da Amazônia](https://www.bancoamazonia.com.br/index.php/o-banco/concursos-e-empregados) | Financeiro | Vagas |
| [Banco Daycoval](https://bancodaycoval.gupy.io) | Financeiro | Gupy |
| [Banco de Brasília (BRB)](https://www.brb.com.br/concursos-e-processos-seletivos) | Financeiro | Vagas |
| [Banco Digio](https://digio.gupy.io) | Financeiro | Gupy |
| [Banco do Brasil](https://www.bb.com.br/pbb/pagina-inicial/sobre-nos/carreiras-no-bb) | Financeiro | Vagas |
| [Banco do Nordeste](https://www.bnb.gov.br/concursos-e-selecoes) | Financeiro | Vagas |
| [Banco Fibra](https://bancofibra.gupy.io) | Financeiro | Gupy |
| [Banco Inbursa](https://www.inbursa.com/BolsadeTrabajo) | Financeiro | Vagas |
| [Banco Industrial do Brasil](https://bib.gupy.io) | Financeiro | Gupy |
| [Banco Inter](https://carreiras.gupy.io/bancointer) | Financeiro | Gupy |
| [Banco Mercantil](https://mercantil.gupy.io) | Financeiro | Gupy |
| [Banco Mercantil do Brasil](https://bancomercantil.gupy.io) | Financeiro | Gupy |
| [Banco Original](https://original.gupy.io) | Financeiro | Gupy |
| [Banco Ourinvest](https://bancoourinvest.gupy.io) | Financeiro | Gupy |
| [Banco Pan](https://boards.greenhouse.io/bancopan) | Financeiro | Greenhouse |
| [Banco Paulista](https://bancopaulista.solides.jobs) | Financeiro | Vagas |
| [Banco Pine](https://bancopine.inhire.app/vagas) | Financeiro | InHire |
| [Banco Rendimento](https://rendimento.gupy.io) | Financeiro | Gupy |
| [Banco Rodobens](https://rodobenscarreiras.gupy.io) | Financeiro | Gupy |
| [Banco Safra](https://safra.gupy.io) | Financeiro | Gupy |
| [Banco Semear](https://www.bancosemear.com.br/trabalhe-conosco) | Financeiro | Vagas |
| [Banco Sofisa](https://bancosofisa.gupy.io) | Financeiro | Gupy |
| [Banco Topázio](https://bancotopazio.gupy.io) | Financeiro | Gupy |
| [Banco Votorantim (banco BV)](https://bv.gupy.io) | Financeiro | Gupy |
| [Band](https://band.jobs.recrut.ai/#openings) | Serviços e Outros | Recrut.ai |
| [Bandai Namco](https://www.bandainamcoent.com/careers) | Serviços e Outros | Site da Empresa |
| [Banestes](https://www.banestes.com.br/trabalhe-conosco) | Financeiro | Vagas |
| [banQi](https://banqi.gupy.io) | Financeiro | Gupy |
| [Banrisul](https://www.banrisul.com.br/concursos) | Financeiro | Vagas |
| [BASF](https://career5.successfactors.eu/career?company=C0000159936P) | Indústria | SuccessFactors |
| [Bauducco](https://bauducco.gupy.io) | Serviços e Outros | Gupy |
| [Bayer](https://bayer.eightfold.ai/careers) | Saúde | Eightfold |
| [BB Seguridade](https://brasilseg.gupy.io) | Financeiro | Gupy |
| [BBC](https://careers.bbc.co.uk) | Serviços e Outros | Site da Empresa |
| [Beep Saúde](https://beepsaude.gupy.io) | Saúde | Gupy |
| [Beleaf](https://www.beleaf.com.br/trabalhe-conosco) | Serviços e Outros | Vagas |
| [Belvo](https://belvo.com/careers) | Financeiro | Lever |
| [Bemobi](https://bemobi.gupy.io) | Tecnologia | Gupy |
| [Beyond 101](https://apply.workable.com/beyond-101) | Tecnologia | Workable |
| [BHS](https://bhs.gupy.io) | Tecnologia | Gupy |
| [Biolab](https://biolabfarma.gupy.io) | Saúde | Gupy |
| [Bitso](https://bitso.com/jobs) | Financeiro | Greenhouse |
| [BizCapital](https://bizcapital.gupy.io) | Financeiro | Gupy |
| [Blackberry](https://www.blackberry.com/us/en/company/careers) | Tecnologia | Site da Empresa |
| [Blau Farmacêutica](https://blau.com.br/carreiras) | Saúde | Vagas |
| [Blip](https://carreiras.gupy.io/blip) | Tecnologia | Gupy |
| [Blizzard](https://activision.wd1.myworkdayjobs.com/Blizzard_External_Careers) | Serviços e Outros | Workday |
| [BMG](https://bmg.gupy.io) | Financeiro | Gupy |
| [BMW Group Brasil](https://bmw.gupy.io) | Indústria | Gupy |
| [BNY Mellon](https://bnymellon.eightfold.ai/careers) | Financeiro | Eightfold |
| [Bold Snacks](https://bold.net/trabalhe-conosco) | Serviços e Outros | Vagas |
| [BoldMetrics](https://boldmetrics.com/careers) | Serviços e Outros | Manual |
| [Bom pra Crédito](https://bompracredito.gupy.io) | Financeiro | Gupy |
| [Booking](https://jobs.booking.com/booking/jobs) | Serviços e Outros | Plataforma Interna |
| [Booking.com](https://jobs.booking.com) | Serviços e Outros | Site da Empresa |
| [Bosch Group](https://careers.smartrecruiters.com/BoschGroup) | Indústria | SmartRecruiters |
| [Boulder Colorado](https://bouldercolorado.wd1.myworkdayjobs.com/en-US/External) | Serviços e Outros | Workday |
| [Box Delivery](https://boxdelivery.gupy.io) | Logística e Mobilidade | Gupy |
| [Bradesco](https://banco.bradesco/trabalheconosco) | Financeiro | Site da Empresa |
| [Bradesco Seguros](https://bradesco.csod.com/ux/ats/careersite/3/home?c=bradesco) | Financeiro | CSOD |
| [BrasilAgro](https://brasilagro.gupy.io) | Agro e Alimentos | Gupy |
| [Brasilprev](https://brasilprev.gupy.io) | Financeiro | Gupy |
| [Braskem](https://epiw.fa.la1.oraclecloud.com/hcmUI/CandidateExperience/pt-BR/sites/CX_1001/requisitions) | Indústria | OracleCloud |
| [Braspress](https://braspress.pandape.infojobs.com.br) | Serviços e Outros | PandaPe |
| [Brastemp (Whirlpool)](https://carreiras.gupy.io/whirlpool) | Serviços e Outros | Gupy |
| [Braze](https://job-boards.greenhouse.io/braze) | Tecnologia | Greenhouse |
| [BRF](https://brf.com/talentos) | Serviços e Outros | Vagas |
| [Brinks Brasil](https://brinks.gupy.io) | Serviços e Outros | Gupy |
| [Brisanet](https://brisanet.gupy.io) | Serviços e Outros | Gupy |
| [BRQ Digital Solutions](https://carreiras.gupy.io/brq) | Tecnologia | Gupy |
| [BTG Pactual](https://boards.greenhouse.io/btgpactual) | Financeiro | Greenhouse |
| [Buffer](https://journey.buffer.com) | Tecnologia | Site da Empresa |
| [Bunge](https://bunge.gupy.io) | Indústria | Gupy |
| [Burger King](https://carreiras.gupy.io/burgerkingbrasil) | Serviços e Outros | Gupy |
| [Burger King (Zamp)](https://zamp.gupy.io) | Serviços e Outros | Gupy |
| [ByteDance](https://jobs.bytedance.com/en) | Tecnologia | Site da Empresa |
| [C&A](https://cea.gupy.io) | Serviços e Outros | Gupy |
| [C&A Brasil](https://ceabrasil.gupy.io) | Serviços e Outros | Gupy |
| [C6 Bank](https://boards.greenhouse.io/c6bank) | Financeiro | Greenhouse |
| [Cabify](https://job-boards.greenhouse.io/cabify) | Serviços e Outros | Greenhouse |
| [Cacau Show](https://cacaushow.gupy.io) | Serviços e Outros | Gupy |
| [Caesb](https://www.caesb.df.gov.br/concursos.html) | Serviços e Outros | Vagas |
| [Caffeine Army](https://caffeinearmy.inhire.app) | Serviços e Outros | Vagas |
| [Cagece](https://www.cagece.com.br/institucional/concursos-e-selecoes) | Serviços e Outros | Vagas |
| [Caixa Econômica Federal](https://www.caixa.gov.br/sobre-a-caixa/trabalhe-na-caixa/concursos) | Financeiro | Vagas |
| [Caixa Seguridade](https://caixaseguridade.gupy.io) | Financeiro | Gupy |
| [Caju](https://caju.gupy.io) | Financeiro | Gupy |
| [Camargo Corrêa](https://camargocorrea.gupy.io) | Serviços e Outros | Gupy |
| [Camicado (Lojas Renner)](https://lojasrenner.gupy.io) | Varejo e Consumo | Gupy |
| [Camil](https://camilalimentos.com.br/carreiras) | Serviços e Outros | Vagas |
| [Camil Alimentos](https://platform.senior.com.br/hcmrs/hcm/curriculo/?tenant=camilcombr&tenantdomain=camil.com.br#!/vacancies/list) | Agro e Alimentos | Sênior |
| [Canva](https://www.canva.com/careers) | Tecnologia | Site da Empresa |
| [Caoa](https://caoa.gupy.io) | Indústria | Gupy |
| [Capco](https://boards.greenhouse.io/capco) | Serviços e Outros | Greenhouse |
| [Capgemini](https://www.capgemini.com/br-pt/carreiras) | Serviços e Outros | Vagas |
| [Cargill](https://careers.cargill.com/en/search-jobs) | Serviços e Outros | Site da Empresa |
| [CargoX](https://cargox.inhire.app/vagas) | Serviços e Outros | InHire |
| [Carrefour Brasil](https://carrefour.gupy.io) | Serviços e Outros | Gupy |
| [Carreira](https://carreira.inhire.com.br) | Tecnologia | InHire |
| [Casa Di Conti](https://casadiconti.gupy.io) | Serviços e Outros | Gupy |
| [Casa e Video Varejo](https://casaevideo.gupy.io) | Varejo e Consumo | Gupy |
| [Casan](https://www.casan.com.br/trabalhe-na-casan) | Serviços e Outros | Vagas |
| [Castrolanda](https://castrolanda.gupy.io) | Serviços e Outros | Gupy |
| [CBA Alumínio](https://cba.gupy.io) | Indústria | Gupy |
| [CCR](https://motiva.gupy.io) | Serviços e Outros | Gupy |
| [CD Projekt Red](https://www.cdprojektred.com/en/jobs) | Serviços e Outros | Site da Empresa |
| [Ceg (Naturgy)](https://www.naturgy.com.br/trabalhe-conosco) | Serviços e Outros | Vagas |
| [Celcoin](https://celcoin.inhire.app/vagas) | Financeiro | InHire |
| [Celesc](https://www.celesc.com.br/trabalhe-na-celesc) | Serviços e Outros | Vagas |
| [Cemig](https://www.cemig.com.br/carreiras) | Serviços e Outros | Vagas |
| [Cencosud Brasil](https://cencosudbrasil.gupy.io) | Serviços e Outros | Gupy |
| [Centauro](https://centaurotalentos.gupy.io) | Serviços e Outros | Gupy |
| [Cheftime](https://cheftime.gupy.io) | Serviços e Outros | Gupy |
| [CI&T](https://jobs.lever.co/ciandt) | Tecnologia | Lever |
| [CIEE SC](https://cieesc.gupy.io) | Serviços e Outros | Gupy |
| [Cielo](https://cielo.inhire.app/vagas) | Financeiro | InHire |
| [Cimed](https://cimed.gupy.io) | Saúde | Gupy |
| [Cinemark](https://cinemark.gupy.io) | Mídia e Entretenimento | Gupy |
| [Cisco](https://careers.cisco.com/global/en) | Tecnologia | Site da Empresa |
| [Citi](https://careers.citigroup.com) | Financeiro | Site da Empresa |
| [CLAMED](https://clamed.gupy.io) | Saúde | Gupy |
| [Claro Brasil](https://carreiras.gupy.io/claro) | Energia e Utilities | Gupy |
| [ClearSale](https://clearsale.gupy.io) | Tecnologia | Gupy |
| [Click Entregas](https://clickentregas.com/trabalhe-conosco) | Logística e Mobilidade | Vagas |
| [Cloudera](https://www.cloudera.com/careers.html) | Tecnologia | Workday |
| [CloudWalk](https://jobs.lever.co/cloudwalk) | Financeiro | Lever |
| [Club Athletico Paranaense](https://athletico.gupy.io) | Serviços e Outros | Gupy |
| [Coamo Agroindustrial](https://carreiras.gupy.io/coamo) | Agro e Alimentos | Gupy |
| [Cobasi](https://cobasi.pandape.infojobs.com.br) | Serviços e Outros | InfoJobs |
| [Coca-Cola Company](https://coke.wd1.myworkdayjobs.com/coca-cola-careers) | Serviços e Outros | Workday |
| [Coca-Cola Femsa](https://femsa.gupy.io) | Serviços e Outros | Gupy |
| [Coca-Cola Femsa BR](https://cocacolafemsabr.gupy.io) | Serviços e Outros | Gupy |
| [Cocal](https://cocal.gupy.io) | Serviços e Outros | Gupy |
| [Cocamar](https://cocamar.gupy.io) | Serviços e Outros | Gupy |
| [Coco Bambu](https://cocobambu.gupy.io) | Serviços e Outros | Gupy |
| [Cogna](https://cogna.gupy.io) | Educação | Gupy |
| [Colgate-Palmolive](https://jobs.colgate.com) | Serviços e Outros | Site da Empresa |
| [Comercial Zaffari](https://czaffari.gupy.io) | Serviços e Outros | Gupy |
| [Condor Super Center](https://condor.gupy.io) | Serviços e Outros | Gupy |
| [ConectCar](https://conectcar.gupy.io) | Serviços e Outros | Gupy |
| [Conta Azul](https://contaazul.inhire.app) | Serviços e Outros | Vagas |
| [Conta Simples](https://contasimples.gupy.io) | Financeiro | Gupy |
| [Contabilizei](https://carreiras.gupy.io/contabilizei) | Financeiro | Gupy |
| [Coop](https://cooperativadeconsumo.pandape.infojobs.com.br) | Serviços e Outros | InfoJobs |
| [Coopercitrus](https://coopercitrus.gupy.io) | Serviços e Outros | Gupy |
| [Cooxupé](https://carreiras.gupy.io/cooxupe) | Serviços e Outros | Gupy |
| [Copacol](https://copacol.com.br/trabalhe-conosco) | Serviços e Outros | Vagas |
| [Copasa](https://www.copasa.com.br/wps/portal/internet/trabalhe-na-copasa) | Serviços e Outros | Vagas |
| [Copel](https://www.copel.com/site/trabalhe-na-copel) | Serviços e Outros | Vagas |
| [Copersucar](https://copersucar.gupy.io) | Serviços e Outros | Gupy |
| [Coplana](https://coplana.gupy.io) | Serviços e Outros | Gupy |
| [Cora](https://cora.inhire.app/vagas) | Financeiro | InHire |
| [Corel](https://www.corel.com/en/careers) | Tecnologia | Site da Empresa |
| [Cortex](https://cortex.gupy.io) | Tecnologia | Gupy |
| [Cosan](https://cosan.gupy.io) | Serviços e Outros | Gupy |
| [Coursera](https://about.coursera.org/careers) | Educação | Site da Empresa |
| [CPFL Energia](https://cpflenergia.gupy.io) | Energia e Utilities | Gupy |
| [Credcrea (Ailos)](https://credcrea.gupy.io) | Financeiro | Gupy |
| [Creditas](https://creditas.gupy.io) | Financeiro | Gupy |
| [Cris Barros](https://crisbarros.gupy.io) | Serviços e Outros | Gupy |
| [Cristália](https://cristalia.gupy.io) | Saúde | Gupy |
| [CrowdStrike](https://www.crowdstrike.com/careers) | Tecnologia | Workday |
| [Cruzeiro do Sul](https://cruzeirodosul.gupy.io) | Educação | Gupy |
| [Cruzeiro do Sul Educacional](https://cruzeirodosuleducacional.gupy.io) | Educação | Gupy |
| [CS Brasil](https://csbrasil.gupy.io) | Serviços e Outros | Gupy |
| [CSN](https://csn.gupy.io) | Indústria | Gupy |
| [Cury](https://cury.gupy.io) | Serviços e Outros | Gupy |
| [CVC Corp](https://cvccorp.gupy.io) | Serviços e Outros | Gupy |
| [CVP (Caixa Vida e Previdência)](https://caixavidaeprevidencia.gupy.io) | Serviços e Outros | Gupy |
| [Cyrela](https://cyrela.gupy.io) | Serviços e Outros | Gupy |
| [Dafiti Tech Br](https://dafiti.gupy.io) | Tecnologia | Gupy |
| [Daki](https://daki.gupy.io) | Serviços e Outros | Gupy |
| [Danone](https://ptapply-danone.icims.com/jobs/search) | Serviços e Outros | iCIMS |
| [Dasa](https://carreiras.gupy.io/dasa) | Saúde | Gupy |
| [DASA Assistencial](https://dasaassistencial.gupy.io) | Saúde | Gupy |
| [DASA Atendimento](https://dasaatendimento.gupy.io) | Saúde | Gupy |
| [DASA Corp](https://dasacorp.gupy.io) | Saúde | Gupy |
| [DASA Diversidade](https://diversidasa.gupy.io) | Saúde | Gupy |
| [DASA Programas de Entrada](https://dasaprogramasdeentrada.gupy.io) | Saúde | Gupy |
| [DASA Tecnologia](https://dasatecnologia.gupy.io) | Saúde | Gupy |
| [Databricks](https://job-boards.greenhouse.io/databricks) | Tecnologia | Greenhouse |
| [DataDog](https://careers.datadoghq.com/all-jobs) | Tecnologia | Plataforma Interna |
| [DataRobot](https://www.datarobot.com/careers) | Tecnologia | Site da Empresa |
| [Daycoval DayCambio](https://daycambio.gupy.io) | Financeiro | Gupy |
| [Daycoval DayCred](https://daycred.gupy.io) | Financeiro | Gupy |
| [dbtLabs](https://job-boards.greenhouse.io/dbtlabsinc) | Tecnologia | Greenhouse |
| [Decathlon](https://carreirasdecathlon.gupy.io) | Serviços e Outros | Gupy |
| [Delivery Much](https://deliverymuch.gupy.io) | Logística e Mobilidade | Gupy |
| [Dell](https://jobs.dell.com/en) | Tecnologia | Workday |
| [Deloitte](https://app.jobconvo.com/pt-br/careers/Deloitte/ddf2b2f5-cc30-4503-8ec8-458f9869e2ba/#join) | Serviços e Outros | Plataforma Interna |
| [Delta Air Lines](https://delta.avature.net/en_US/careers) | Serviços e Outros | Avature |
| [Descomplica](https://carreiras.gupy.io/descomplica) | Tecnologia | Gupy |
| [Desinchá](https://desincha.com.br/pages/trabalhe-conosco) | Serviços e Outros | Vagas |
| [Desktop](https://desktop.gupy.io) | Serviços e Outros | Gupy |
| [Dexco](https://dexco.gupy.io) | Indústria | Gupy |
| [DiDi (99)](https://careers-didiglobal.icims.com/jobs/search?ss=1&hashed=-625919479) | Serviços e Outros | Plataforma Interna |
| [Diferente](https://diferente.com.br/trabalhe-conosco) | Serviços e Outros | Vagas |
| [Digibee](https://digibee.gupy.io) | Tecnologia | Gupy |
| [Direcional](https://direcional.gupy.io) | Serviços e Outros | Gupy |
| [dLocal](https://jobs.lever.co/dlocal) | Financeiro | Lever |
| [Dock](https://dock.gupy.io) | Serviços e Outros | Gupy |
| [Docket](https://docket.gupy.io) | Tecnologia | Gupy |
| [Docs](https://docs.inhire.com.br) | Tecnologia | InHire |
| [Domino s Pizza](https://dominospizzabrasil.pandape.infojobs.com.br) | Serviços e Outros | PandaPe |
| [Domo](https://www.domo.com/company/careers) | Tecnologia | Site da Empresa |
| [Donorbox](https://job-boards.greenhouse.io/donorbox) | Tecnologia | Greenhouse |
| [DoorDash International](https://boards.greenhouse.io/doordashinternational) | Financeiro | Greenhouse |
| [Dotz](https://dotz.gupy.io) | Financeiro | Gupy |
| [Dr. Consulta](https://carreiras.gupy.io/drconsulta) | Tecnologia | Gupy |
| [Droga Raia / Drogasil (RD Saúde)](https://carreiras.gupy.io/rd) | Saúde | Gupy |
| [Dropbox](https://dropbox.jobs) | Tecnologia | Greenhouse |
| [DRUID Creative Gaming](https://druid.gupy.io) | Serviços e Outros | Gupy |
| [DuckDuckGo](https://jobs.ashbyhq.com/duck-duck-go) | Tecnologia | Ashby |
| [Duolingo](https://careers.duolingo.com) | Educação | Site da Empresa |
| [EA (Electronic Arts)](https://www.ea.com/careers) | Serviços e Outros | Site da Empresa |
| [Eaton](https://eaton.eightfold.ai/careers) | Indústria | Eightfold |
| [Ebanx](https://boards.greenhouse.io/ebanx) | Financeiro | Greenhouse |
| [EcoRodovias](https://ecorodovias.gupy.io) | Serviços e Outros | Gupy |
| [Ecossistema ARGENTA](https://argenta.gupy.io) | Serviços e Outros | Gupy |
| [Edenred (Ticket)](https://wd3.myworkdaysite.com/pt-BR/recruiting/edenpeople/Edenred_Careers) | Financeiro | Workday |
| [EDP Brasil](https://jobs.edp.com) | Serviços e Outros | Portal |
| [Efí Bank](https://sejaefi.gupy.io) | Financeiro | Gupy |
| [Eightfold](https://pepsico.eightfold.ai/careers) | Tecnologia | Eightfold |
| [Electrolux](https://career.electroluxgroup.com) | Serviços e Outros | Manual |
| [Electronic Arts](https://jobs.ea.com/en_US/careers) | Serviços e Outros | Plataforma Interna |
| [Eletrobras](https://eletrobras.gupy.io) | Serviços e Outros | Gupy |
| [Eleva Educação](https://escolaseleva.gupy.io) | Educação | Gupy |
| [Elgin](https://sejaelgin.gupy.io) | Serviços e Outros | Gupy |
| [Elo](https://vempraelo.gupy.io) | Financeiro | Gupy |
| [Embaré](https://embare.com.br/trabalhe-conosco) | Serviços e Outros | Vagas |
| [Embasa](https://www.embasa.ba.gov.br/institucional/concursos) | Serviços e Outros | Vagas |
| [Embraer](https://embraer.gupy.io) | Indústria | Gupy |
| [Emirates](https://www.emiratesgroupcareers.com) | Serviços e Outros | Site da Empresa |
| [EMS](https://ems.izirh.io) | Saúde | IziRH |
| [Energisa (Corp)](https://grupoenergisa.gupy.io) | Serviços e Outros | Gupy |
| [Energisa (Tecnologia)](https://energisatech.gupy.io) | Serviços e Outros | Gupy |
| [Eneva](https://eneva.gupy.io) | Serviços e Outros | Gupy |
| [Engie Brasil](https://jobs.engie.com) | Serviços e Outros | Portal |
| [Enjoei](https://enjoei.gupy.io) | Serviços e Outros | Gupy |
| [Epic Games](https://www.epicgames.com/site/en-US/careers) | Mídia e Entretenimento | Avature |
| [Epson](https://epson.com.br/carreiras) | Tecnologia | Site da Empresa |
| [Equatorial Energia](https://equatorialenergia.gupy.io) | Energia e Utilities | Gupy |
| [Ericsson](https://www.ericsson.com/en/careers) | Serviços e Outros | Site da Empresa |
| [Eternit](https://eternit.gupy.io) | Indústria | Gupy |
| [Eu Entrego](https://www.euentrego.com/entregador) | Serviços e Outros | Vagas |
| [Eurofarma](https://eurofarma.gupy.io) | Saúde | Gupy |
| [Even](https://even.gupy.io) | Serviços e Outros | Gupy |
| [Expedia](https://careers.expediagroup.com) | Serviços e Outros | Site da Empresa |
| [ExxonMobil](https://jobs.exxonmobil.com) | Serviços e Outros | Site da Empresa |
| [EY](https://www.ey.com/pt_br/careers) | Serviços e Outros | GigNow |
| [EZTEC](https://eztec.gupy.io) | Serviços e Outros | Gupy |
| [Faber-Castell](https://fabercastell.gupy.io) | Serviços e Outros | Gupy |
| [Facchini](https://facchini.com.br/trabalhe-conosco) | Indústria | Vagas |
| [Fanatee](https://fanatee.com/#careers) | Serviços e Outros | Plataforma Interna |
| [Farm Moda Br](https://farm.gupy.io) | Varejo e Consumo | Gupy |
| [Fast Shop](https://fastshop.gupy.io) | Serviços e Outros | Gupy |
| [Fazenda Futuro (Future Farm)](https://fazendafuturo.gupy.io) | Serviços e Outros | Gupy |
| [Federação Paulista de Futebol](https://oportunidades.mindsight.com.br/fpf) | Serviços e Outros | Mindsight |
| [FedEx](https://fedex.wd1.myworkdayjobs.com/FXE-EU_External) | Serviços e Outros | Workday |
| [Feedz](https://feedz.inhire.app/vagas) | Tecnologia | InHire |
| [Ferbasa](https://ferbasa.gupy.io) | Serviços e Outros | Gupy |
| [Ferrero](https://www.ferrerocareers.com) | Serviços e Outros | Site da Empresa |
| [FGV - Fundação Getulio Vargas](https://portal.fgv.br/trabalhe-conosco) | Educação | Manual |
| [FIAP](https://alura-fiap-pm3.inhire.app/vagas) | Educação | InHire |
| [Figma](https://boards.greenhouse.io/figma) | Tecnologia | Greenhouse |
| [Flash](https://flash.inhire.app/vagas) | Tecnologia | InHire |
| [Fleury](https://grupofleury.gupy.io) | Saúde | Gupy |
| [Fluency Academy](https://fluencyacademy.gupy.io) | Educação | Gupy |
| [Folha da Manhã](https://folhadespaulo.gupy.io) | Serviços e Outros | Gupy |
| [Food to Save](https://foodtosave.gupy.io) | Serviços e Outros | Gupy |
| [Ford](https://efds.fa.em5.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/requisitions) | Indústria | OracleCloud |
| [Fortinet](https://www.fortinet.com/corporate/careers) | Tecnologia | Site da Empresa |
| [Fortlev](https://fortlev.gupy.io) | Indústria | Gupy |
| [Four Seasons Hotels](https://fourseasons.wd3.myworkdayjobs.com/Search) | Serviços e Outros | Workday |
| [Fox Corporation](https://www.foxcareers.com) | Serviços e Outros | Site da Empresa |
| [Foxbit](https://foxbit.gupy.io) | Financeiro | Gupy |
| [Franq](https://franq.gupy.io) | Financeiro | Gupy |
| [Fras-le](https://randoncorp.gupy.io) | Indústria | Gupy |
| [Frete.com](https://frete.gupy.io) | Serviços e Outros | Gupy |
| [Fretebras](https://fretebras.inhire.app/vagas) | Serviços e Outros | InHire |
| [Frimesa](https://www.frimesa.com.br/pt/trabalhe-conosco) | Serviços e Outros | Vagas |
| [Frooty](https://frooty.gupy.io) | Serviços e Outros | Gupy |
| [FSG Centro Universitário](https://fsg.gupy.io) | Educação | Gupy |
| [Fundação Bradesco](https://bradesco.csod.com/ux/ats/careersite/2/home?c=bradesco) | Educação | CSOD |
| [Fundação Itaú](https://fundacaoitau.gupy.io) | Financeiro | Gupy |
| [Fundação Pedro Paes Mendonça](https://fppm.gupy.io) | Serviços e Outros | Gupy |
| [Fundação São Paulo (FUNDASP)](https://fundasp.gupy.io) | Educação | Gupy |
| [Gafisa](https://gafisa.gupy.io) | Serviços e Outros | Gupy |
| [Gamers Club](https://gamersclub.gupy.io) | Mídia e Entretenimento | Gupy |
| [Garena](https://careers.garena.com/global/careers) | Serviços e Outros | Plataforma Interna |
| [Gazin](https://gazin.gupy.io) | Serviços e Outros | Gupy |
| [GE (General Electric)](https://jobs.gecareers.com) | Indústria | Workday |
| [GE Aerospace](https://careers.geaerospace.com/global/en/search-results) | Tecnologia | Plataforma Interna |
| [GE Healthcare](https://careers.gehealthcare.com) | Saúde | Phenom |
| [GE Vernova](https://careers.gevernova.com/global/en/search-results) | Tecnologia | Plataforma Interna |
| [General Motors](https://search-careers.gm.com) | Indústria | Workday |
| [Genial Investimentos](https://genial.gupy.io) | Serviços e Outros | Gupy |
| [Gerador](https://gerador.inhire.com.br) | Tecnologia | InHire |
| [Gerdau](https://career19.sapsf.com/careers?company=gerdauacos) | Indústria | SAP SuccessFactors |
| [Geru](https://open-co.gupy.io) | Financeiro | Gupy |
| [Getnet](https://getnet.gupy.io) | Financeiro | Gupy |
| [GFT Tecnologia](https://career5.successfactors.eu/careers?company=gfttechnol) | Serviços e Outros | SAP SuccessFactors |
| [Gigster](https://virtasant.teamtailor.com) | Tecnologia | Teamtailor |
| [Giross](https://giross.gupy.io) | Serviços e Outros | Gupy |
| [GitHub](https://github.com/about/careers) | Tecnologia | Site da Empresa |
| [GitHub Inc](https://globalcareers-githubinc.icims.com/jobs) | Tecnologia | iCIMS |
| [Globo](https://globo.gupy.io) | Serviços e Outros | Gupy |
| [GM Financial](https://careers.gmfinancial.com/jobs) | Serviços e Outros | Workday |
| [GOL Linhas Aéreas](https://golcarreiras.gupy.io) | Serviços e Outros | Gupy |
| [Google](https://www.google.com/about/careers/applications/jobs/results) | Tecnologia | Plataforma Interna |
| [GoPro](https://gopro.com/en/us/careers) | Tecnologia | Greenhouse |
| [Gorila](https://carreiras.gupy.io/gorila) | Financeiro | Gupy |
| [GPA](https://corporacaogpa.gupy.io) | Serviços e Outros | Gupy |
| [Grammarly](https://www.grammarly.com/jobs) | Tecnologia | Site da Empresa |
| [Granado](https://granado.gupy.io) | Serviços e Outros | Gupy |
| [Granero](https://granero.gupy.io) | Serviços e Outros | Gupy |
| [Greenhouse](https://job-boards.greenhouse.io/greenhouse) | Tecnologia | Greenhouse |
| [Grendene](https://grendene.gupy.io) | Indústria | Gupy |
| [Gringo](https://gringo.inhire.app/vagas) | Serviços e Outros | InHire |
| [Grupo Águia Branca](https://grupoaguiabranca.gupy.io) | Serviços e Outros | Gupy |
| [Grupo Bertolini](https://bertolini.gupy.io) | Indústria | Gupy |
| [Grupo Boticário](https://grupoboticario.gupy.io) | Serviços e Outros | Gupy |
| [Grupo Carrefour](https://corporativo-grupocarrefourbrasil.pandape.infojobs.com.br) | Serviços e Outros | InfoJobs |
| [Grupo Casas Bahia](https://carreiras.gupy.io/grupocasasbahia) | Serviços e Outros | Gupy |
| [Grupo Despegar (Decolar.com)](https://jobs.lever.co/despegar) | Serviços e Outros | Lever |
| [Grupo Gontijo](https://gontijo.gupy.io) | Serviços e Outros | Gupy |
| [Grupo Habib's](https://grupohabibs.pandape.infojobs.com.br) | Serviços e Outros | InfoJobs |
| [Grupo L'Occitane](https://sejaloccitane.gupy.io) | Serviços e Outros | Gupy |
| [Grupo Marilan](https://marilan.gupy.io) | Serviços e Outros | Gupy |
| [Grupo Mateus](https://grupomateus.gupy.io) | Serviços e Outros | Gupy |
| [Grupo Muffato](https://grupomuffatovagas.gupy.io) | Serviços e Outros | Gupy |
| [Grupo NC](https://gruponc.gupy.io) | Serviços e Outros | Gupy |
| [Grupo Nós](https://gruponos.gupy.io) | Serviços e Outros | Gupy |
| [Grupo Primo](https://jobs.quickin.io/grupo-primo/jobs) | Serviços e Outros | Quickin |
| [Grupo RV](https://gruporv.pandape.infojobs.com.br) | Serviços e Outros | InfoJobs |
| [Grupo Sabin](https://gruposabin.gupy.io) | Saúde | Gupy |
| [Grupo SEB](https://gruposeb.gupy.io) | Educação | Gupy |
| [Grupo Silvio Santos](https://gruposilviosantos.gupy.io) | Serviços e Outros | Gupy |
| [Grupo Soma](https://gruposoma.gupy.io) | Serviços e Outros | Gupy |
| [Grupo Zaffari](https://grupozaffari.gupy.io) | Serviços e Outros | Gupy |
| [Guanabara](https://guanabara.gupy.io) | Serviços e Outros | Gupy |
| [Gupy](https://vempra.gupy.io) | Tecnologia | Gupy |
| [Gupy Tech](https://tech-career.gupy.io) | Tecnologia | Gupy |
| [Gupy Tecnologia](https://gupy.gupy.io) | Serviços e Outros | Gupy |
| [Habib s](https://carreiras.gupy.io/habibs) | Serviços e Outros | Gupy |
| [Hapvida NotreDame Intermédica](https://hapvidandi.pandape.infojobs.com.br) | Saúde | InfoJobs |
| [Hashdex](https://hashdex.gupy.io) | Serviços e Outros | Gupy |
| [Havan](https://havan.gupy.io) | Serviços e Outros | Gupy |
| [HBO (Warner Bros. Discovery)](https://careers.wbd.com/global/en) | Serviços e Outros | Site da Empresa |
| [HBR Realty](https://hbrrealty.gupy.io) | Serviços e Outros | Gupy |
| [HDI Seguros](https://hdiseguros.gupy.io) | Financeiro | Gupy |
| [Heineken](https://careers.theheinekencompany.com/Brazil/search) | Serviços e Outros | SuccessFactors |
| [Helbor](https://helbor.gupy.io) | Serviços e Outros | Gupy |
| [Henry Schein Brasil](https://henryschein.gupy.io) | Saúde | Gupy |
| [Hering](https://ciahering.gupy.io) | Serviços e Outros | Gupy |
| [Hidrovias do Brasil](https://hidrovias.gupy.io) | Serviços e Outros | Gupy |
| [Hilton](https://jobs.hilton.com) | Serviços e Outros | Site da Empresa |
| [Hinode](https://hinode.gupy.io) | Serviços e Outros | Gupy |
| [Honda](https://honda.gupy.io) | Indústria | Gupy |
| [Hootsuite](https://careers.hootsuite.com) | Tecnologia | Manual |
| [Hopper](https://www.hopper.com/careers) | Serviços e Outros | Site da Empresa |
| [Hospital Care](https://hospitalcare.gupy.io) | Saúde | Gupy |
| [Hospital IGESP](https://www.vagas.com.br/vagas-de-igesp) | Saúde | Vagas |
| [Hospital Moinhos de Vento](https://hospitalmoinhos.gupy.io) | Saúde | Gupy |
| [Hospital Sírio-Libanês](https://career19.sapsf.com/careers?company=sociedad02) | Saúde | SAP SuccessFactors |
| [Hotmart](https://boards.eu.greenhouse.io/hotmartcareersbr) | Tecnologia | Greenhouse |
| [HubSpot](https://www.hubspot.com/careers) | Tecnologia | Site da Empresa |
| [Hyatt](https://careers.hyatt.com) | Serviços e Outros | Site da Empresa |
| [Hyland](https://careers-hyland.icims.com/jobs/search?ss=1&hashed=-435679902) | Tecnologia | iCIMS |
| [Hypera Pharma](https://hyperapharma.gupy.io) | Saúde | Gupy |
| [IBM](https://www.ibm.com/br-pt/careers) | Tecnologia | Brasio |
| [Icatu Seguros](https://icatuseguros.gupy.io) | Financeiro | Gupy |
| [ICI Curitiba](https://ici.gupy.io) | Tecnologia | Gupy |
| [ICIMS](https://careers.icims.com/careers-home/jobs) | Tecnologia | Plataforma Interna |
| [iFood](https://job-boards.greenhouse.io/ifoodcarreiras) | Serviços e Outros | Greenhouse |
| [Iguatemi](https://iguatemi.gupy.io) | Serviços e Outros | Gupy |
| [Ilegra](https://vagas.ilegra.com) | Tecnologia | Plataforma Interna |
| [ília](https://boards.greenhouse.io/ilia) | Serviços e Outros | Greenhouse |
| [Infracommerce](https://infracommerce.gupy.io) | Serviços e Outros | Gupy |
| [Inkrypton](https://inkrypton.inhire.com.br) | Tecnologia | InHire |
| [Intel](https://jobs.intel.com) | Tecnologia | Manual |
| [Intelipost](https://intelipost.gupy.io) | Serviços e Outros | Gupy |
| [Inter](https://boards.greenhouse.io/inter) | Financeiro | Greenhouse |
| [Intera](https://vagasbyintera.inhire.app/vagas) | Financeiro | InHire |
| [Involves](https://involves.inhire.app/vagas) | Serviços e Outros | InHire |
| [Ipiranga](https://ipiranga.gupy.io) | Serviços e Outros | Gupy |
| [iPlace](https://iplace.gupy.io) | Serviços e Outros | Gupy |
| [IQVIA](https://jobs.iqvia.com/en/search-jobs) | Serviços e Outros | Plataforma Interna |
| [Irani Papel e Embalagem](https://irani.gupy.io) | Serviços e Outros | Gupy |
| [Isa CTEEP](https://isacteep.gupy.io) | Serviços e Outros | Gupy |
| [Isaac](https://boards.greenhouse.io/isaac) | Financeiro | Greenhouse |
| [Itambé](https://itambe.gupy.io) | Serviços e Outros | Gupy |
| [Itapemirim (Nova Itapemirim)](https://novaitapemirim.gupy.io) | Serviços e Outros | Gupy |
| [Itaú](https://vemproitau.gupy.io) | Financeiro | Gupy |
| [Itaú - Carreiras Internas](https://carreirasinternasitau.gupy.io) | Financeiro | Gupy |
| [Itaú Cultural](https://itaucultural.gupy.io) | Financeiro | Gupy |
| [Itaú Social](https://itausocial.gupy.io) | Serviços e Outros | Gupy |
| [Itaú Unibanco](https://itau.gupy.io) | Financeiro | Gupy |
| [ITV](https://www.itvjobs.com) | Serviços e Outros | Site da Empresa |
| [Iugu](https://iugu.inhire.app/vagas) | Financeiro | InHire |
| [JBS](https://grupojbs.gupy.io) | Serviços e Outros | Gupy |
| [JD.com](https://corporate.jd.com/careers) | Serviços e Outros | Site da Empresa |
| [Jequiti](https://jequiti.gupy.io) | Serviços e Outros | Gupy |
| [JHSF](https://jhsf.gupy.io) | Serviços e Outros | Gupy |
| [João Fortes](https://joaofortes.gupy.io) | Serviços e Outros | Gupy |
| [John Deere](https://johndeere.eightfold.ai/careers) | Indústria | Eightfold |
| [Johnson & Johnson](https://www.careers.jnj.com) | Saúde | Workday |
| [JPMorgan Chase](https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/requisitions) | Financeiro | OracleCloud |
| [JSL](https://jsl.gupy.io) | Serviços e Outros | Gupy |
| [Jungle](https://jungle.gupy.io) | Serviços e Outros | Gupy |
| [JusBrasil](https://boards.greenhouse.io/jusbrasil) | Tecnologia | Greenhouse |
| [Kalunga](https://kalunga.pandape.infojobs.com.br) | Serviços e Outros | Vagas |
| [Kanastra](https://kanastra.inhire.app/vagas) | Financeiro | InHire |
| [Kangu](https://kangu.gupy.io) | Serviços e Outros | Gupy |
| [Kaspersky](https://careers.kaspersky.com) | Tecnologia | Site da Empresa |
| [Kavak](https://kavakcom.pandape.infojobs.com.br) | Indústria | InfoJobs |
| [Kepler Weber](https://keplerweber.gupy.io) | Serviços e Outros | Gupy |
| [Keyrus](https://jobs.keyrus.com.br/jobs) | Serviços e Outros | Plataforma Interna |
| [Khan Academy](https://www.khanacademy.org/about/careers) | Educação | Site da Empresa |
| [Kimberly-Clark](https://kimberlyclark.wd1.myworkdayjobs.com/GLOBAL) | Serviços e Outros | Workday |
| [Kiwify](https://kiwify.inhire.app/vagas) | Tecnologia | InHire |
| [Klabin](https://klabin.inhire.app/vagas) | Indústria | InHire |
| [KMM](https://kmm.gupy.io) | Serviços e Outros | Gupy |
| [Kora Saúde](https://korasaude.gupy.io) | Saúde | Gupy |
| [Korp ERP](https://korp.gupy.io) | Tecnologia | Gupy |
| [Kovi](https://kovi.gupy.io) | Serviços e Outros | Gupy |
| [KPMG](https://kpmg.com/br/pt/home/carreiras.html) | Serviços e Outros | Avature |
| [KPMG Brasil](https://carreira.inhire.com.br/carreiras/kpmg) | Serviços e Outros | InHire |
| [Kraft Heinz](https://careers.kraftheinz.com/job-search-results) | Serviços e Outros | Plataforma Interna |
| [KRYPTUS](https://kryptus.gupy.io) | Tecnologia | Gupy |
| [Kwan](https://kwan.com/careers/#jobpost) | Tecnologia | Plataforma Interna |
| [Lalamove Brasil](https://lalamove.gupy.io) | Serviços e Outros | Gupy |
| [Lar Cooperativa](https://www.lar.ind.br/trabalhe-conosco) | Serviços e Outros | Vagas |
| [Launchpad Technologies](https://job-boards.greenhouse.io/launchpadtechnologiesinc) | Tecnologia | Greenhouse |
| [Lavvi](https://lavvi.gupy.io) | Serviços e Outros | Gupy |
| [Le Biscuit Varejo](https://lebiscuit.gupy.io) | Varejo e Consumo | Gupy |
| [LEGO](https://lego.wd103.myworkdayjobs.com/LEGO_External) | Tecnologia | Workday |
| [Lenovo](https://jobs.lenovo.com) | Tecnologia | Site da Empresa |
| [Leroy Merlin](https://carreiras.leroymerlin.com.br) | Serviços e Outros | Site da Empresa |
| [Letrus](https://letrus.inhire.app/vagas) | Tecnologia | InHire |
| [Leve Saúde](https://levesaude.gupy.io) | Saúde | Gupy |
| [LevelUp](https://trampos.co/level-up) | Serviços e Outros | Plataforma Interna |
| [Levo](https://levo.gupy.io) | Serviços e Outros | Gupy |
| [LG](https://www.lg.com/global/careers) | Tecnologia | Manual |
| [LG Electronics do Brasil LTDA](https://lge.gupy.io) | Serviços e Outros | Gupy |
| [Libbs](https://libbs.gupy.io) | Serviços e Outros | Gupy |
| [Liberty Seguros](https://libertyseguros.gupy.io) | Financeiro | Gupy |
| [Librelato](https://www.librelato.com.br/trabalhe-conosco) | Serviços e Outros | Vagas |
| [Light](https://www.light.com.br/grupo-light/Trabalhe-na-Light/default.aspx) | Serviços e Outros | Vagas |
| [LinkedIn](https://careers.linkedin.com) | Tecnologia | Site da Empresa |
| [LinkedIn Brasil](https://linkedin.gupy.io) | Tecnologia | Gupy |
| [Linx](https://carreiras.gupy.io/linx) | Tecnologia | Gupy |
| [Liv Up](https://livup.gupy.io) | Serviços e Outros | Gupy |
| [Live Nation](https://www.livenationentertainment.com/careers) | Serviços e Outros | Workday |
| [Livelo](https://livelo.gupy.io) | Financeiro | Gupy |
| [Local Frio](https://localfrio.gupy.io) | Serviços e Outros | Gupy |
| [Localiza](https://localiza.gupy.io) | Serviços e Outros | Gupy |
| [Locaweb](https://locaweb.gupy.io) | Tecnologia | Gupy |
| [Loews Hotels](https://www.loewshotels.com/careers) | Serviços e Outros | Site da Empresa |
| [Loft](https://loft.teamtailor.com/jobs) | Tecnologia | TeamTailor |
| [Log Commercial Properties](https://log.gupy.io) | Serviços e Outros | Gupy |
| [Loggi](https://apply.workable.com/loggi) | Serviços e Outros | Workable |
| [Loggi Tecnologia](https://loggi.gupy.io) | Serviços e Outros | Gupy |
| [Login Logística](https://login.gupy.io) | Logística e Mobilidade | Gupy |
| [Logitech](https://www.logitech.com/careers) | Tecnologia | Manual |
| [Lojas Cem](https://www.lojascem.com.br/trabalhe-conosco) | Varejo e Consumo | Vagas |
| [Lojas Quero-Quero](https://www.queroquero.com.br/trabalhe-conosco) | Varejo e Consumo | Vagas |
| [Lojas Renner S.A.](https://encantech.gupy.io) | Varejo e Consumo | Gupy |
| [Lojas Ypê](https://carreirasype.gupy.io) | Varejo e Consumo | Gupy |
| [LOUD](https://loud.gupy.io) | Serviços e Outros | Gupy |
| [Lufthansa](https://www.lufthansagroup.careers) | Serviços e Outros | Site da Empresa |
| [M. Dias Branco](https://mdiasbranco.gupy.io) | Serviços e Outros | Gupy |
| [Mackenzie](https://mackenzie.br/trabalhe-conosco) | Educação | Site da Empresa |
| [MadeiraMadeira](https://carreiras.gupy.io/madeiramadeira) | Serviços e Outros | Gupy |
| [Madero](https://carreiras.gupy.io/madero) | Serviços e Outros | Gupy |
| [Magalu](https://magazineluiza.inhire.app) | Serviços e Outros | InHire |
| [Magazine Luiza](https://99jobs.com/magazine-luiza) | Serviços e Outros | Vagas |
| [Magnetis](https://magnetis.gupy.io) | Serviços e Outros | Gupy |
| [Mais Mu](https://maismu.gupy.io) | Serviços e Outros | Gupy |
| [Mapfre Brasil](https://www.mapfre.com.br/trabalhe-na-mapfre) | Serviços e Outros | Vagas |
| [Marcopolo](https://www.marcopolo.com.br/carreiras) | Indústria | Vagas |
| [Marfrig](https://www.marfrig.com.br/pt/trabalhe-conosco) | Serviços e Outros | Vagas |
| [Maria Filó Moda Br](https://mariafilo.gupy.io) | Varejo e Consumo | Gupy |
| [Marisa](https://carreiras.gupy.io/marisa) | Serviços e Outros | Gupy |
| [Marisol](https://marisol.gupy.io) | Serviços e Outros | Gupy |
| [Marriott International](https://jobs.marriott.com) | Serviços e Outros | Site da Empresa |
| [Mart Minas](https://martminas.com.br/trabalhe-conosco) | Serviços e Outros | Vagas |
| [Martins Atacado Var](https://martins.gupy.io) | Agro e Alimentos | Gupy |
| [Mash](https://mash.pandape.infojobs.com.br) | Serviços e Outros | InfoJobs |
| [Mastercard](https://mastercard.wd1.myworkdayjobs.com/CorporateCareers) | Financeiro | Workday |
| [MasterClass](https://boards.greenhouse.io/masterclass) | Serviços e Outros | Greenhouse |
| [Mater Dei](https://materdei.gupy.io) | Serviços e Outros | Gupy |
| [McDonalds (Corporativo)](https://corporativomc.gupy.io) | Serviços e Outros | Gupy |
| [Meituan](https://zhaopin.meituan.com/en) | Tecnologia | Site da Empresa |
| [Melhor Envio](https://melhorenvio.gupy.io) | Serviços e Outros | Gupy |
| [Melhoramentos](https://melhoramentos.gupy.io) | Serviços e Outros | Gupy |
| [Meliuz](https://meliuz.inhire.app/vagas) | Financeiro | InHire |
| [Méliuz](https://meliuz.greenhouse.io) | Serviços e Outros | Vagas |
| [Méliuz Brasil Tech](https://meliuz.gupy.io) | Tecnologia | Gupy |
| [Melnick](https://melnick.gupy.io) | Serviços e Outros | Gupy |
| [Mercado Bitcoin](https://mercadobitcoin.inhire.app/vagas) | Financeiro | InHire |
| [Mercado Livre](https://mercadolibre.eightfold.ai/careers) | Serviços e Outros | Eightfold |
| [Mercedes-Benz Brasil](https://mercedes-benz.gupy.io) | Indústria | Gupy |
| [Mercedes-Benz Caminhões & Ônibus (Externa)](https://mercedes-benzcaminhoeseonibus.gupy.io) | Indústria | Gupy |
| [Metha (antiga OAS)](https://metha.gupy.io) | Serviços e Outros | Gupy |
| [Michelin](https://michelinhr.wd3.myworkdayjobs.com/Michelin) | Indústria | Workday |
| [Microsoft](https://careers.microsoft.com) | Tecnologia | Site da Empresa |
| [Mills](https://mills.gupy.io) | Serviços e Outros | Gupy |
| [Mimic](https://mimic.gupy.io) | Serviços e Outros | Gupy |
| [Mindbody](https://co.mindbodyonline.com/careers/opportunities) | Tecnologia | Plataforma Interna |
| [Mineirao Atacarejo](https://mineirao.gupy.io) | Serviços e Outros | Gupy |
| [Minerva Foods](https://minervafoods.gupy.io) | Serviços e Outros | Gupy |
| [Mitre Realty](https://mitrerealty.gupy.io) | Serviços e Outros | Gupy |
| [MJV](https://mjv.inhire.app/vagas) | Serviços e Outros | InHire |
| [Mobit Tecnologia](https://mobit.gupy.io) | Serviços e Outros | Gupy |
| [Mobly](https://mobly.gupy.io) | Serviços e Outros | Gupy |
| [Mombora](https://mombora.gupy.io) | Serviços e Outros | Gupy |
| [Mondelez Brasil](https://mondelez.gupy.io) | Serviços e Outros | Gupy |
| [Mondelez Internacional](https://wd3.myworkdaysite.com/en-US/recruiting/mdlz/External) | Financeiro | Workday |
| [Mondial Eletrodomésticos](https://selecaogrupomk.vagas.solides.com.br) | Serviços e Outros | SOLIDES |
| [Monte Carlo Moda](https://montecarlo.gupy.io) | Varejo e Consumo | Gupy |
| [Motorola Solutions](https://motorolasolutions.wd5.myworkdayjobs.com/Careers) | Tecnologia | Workday |
| [Mottu](https://mottu.inhire.app) | Serviços e Outros | Vagas |
| [Moura Dubeux](https://mouradubeux.gupy.io) | Serviços e Outros | Gupy |
| [Movida](https://movida.gupy.io) | Indústria | Gupy |
| [MRS Logística](https://www.mrs.com.br/trabalhe-conosco) | Logística e Mobilidade | Vagas |
| [MRV](https://www.mrv.com.br/trabalhe-conosco) | Serviços e Outros | Manual |
| [Multilog](https://multilog.gupy.io) | Serviços e Outros | Gupy |
| [Multiplan](https://multiplan.gupy.io) | Serviços e Outros | Gupy |
| [Mutant](https://mutantbrvagas.gupy.io) | Tecnologia | Gupy |
| [Nadara](https://nadara.wd3.myworkdayjobs.com/External) | Tecnologia | Workday |
| [Natura&CO (Avon + The Body Shop)](https://avon.wd5.myworkdayjobs.com/NaturaCarreiras) | Serviços e Outros | Workday |
| [Nazária](https://nazaria.gupy.io) | Serviços e Outros | Gupy |
| [NBCUniversal](https://www.nbcunicareers.com) | Serviços e Outros | Site da Empresa |
| [Neoenergia](https://carreiras.gupy.io/neoenergia) | Energia e Utilities | Gupy |
| [Neogrid](https://neogrid.gupy.io) | Serviços e Outros | Gupy |
| [Neon](https://jobs.lever.co/neon) | Financeiro | Lever |
| [Nestlé](https://jobdetails.nestle.com) | Serviços e Outros | SuccessFactors |
| [Netbr](https://careers.smartrecruiters.com/Netbr) | Tecnologia | SmartRecruiters |
| [Netflix](https://jobs.netflix.com) | Serviços e Outros | Site da Empresa |
| [Neurotech](https://neurotech.jobs.recrut.ai/#openings) | Tecnologia | Recrut.ai |
| [New](https://new.inhire.com.br) | Tecnologia | InHire |
| [Nissan](https://www.nissan.com.br/trabalhe-conosco.html) | Indústria | Site da Empresa |
| [Nita Alimentos](https://nitaalimentos.gupy.io) | Agro e Alimentos | Gupy |
| [Nomad](https://carreiras.gupy.io/nomad) | Financeiro | Gupy |
| [Nomad Global](https://apply.workable.com/nomadglobal) | Tecnologia | Workable |
| [Notion](https://jobs.ashbyhq.com/notion) | Tecnologia | Ashby |
| [NovaDAX](https://novadax.gupy.io) | Serviços e Outros | Gupy |
| [Novo](https://novo.inhire.com.br) | Tecnologia | InHire |
| [Novonor (Odebrecht)](https://novonor.gupy.io) | Serviços e Outros | Gupy |
| [NTT Data](https://careers.emeal.nttdata.com/s/jobs?language=pt_BR) | Tecnologia | Plataforma Interna |
| [Nubank](https://boards.greenhouse.io/nubank) | Financeiro | Greenhouse |
| [Nubank (Nu Holdings)](https://nubank.greenhouse.io) | Financeiro | Vagas |
| [Nude.](https://nude.gupy.io) | Serviços e Outros | Gupy |
| [O Estado de S. Paulo](https://estadao.gupy.io) | Serviços e Outros | Gupy |
| [Oakberry](https://oakberry.gupy.io) | Serviços e Outros | Gupy |
| [OdontoPrev](https://odontoprev.gupy.io) | Saúde | Gupy |
| [Odous de Deus](https://odousdedeus.gupy.io) | Saúde | Gupy |
| [OEC](https://oec.gupy.io) | Serviços e Outros | Gupy |
| [OEC (Odebrecht)](https://oec-eng.com/trabalhe-conosco) | Serviços e Outros | Site da Empresa |
| [Olga Ri](https://olgari.gupy.io) | Serviços e Outros | Gupy |
| [Olist](https://olist.inhire.app/vagas) | Tecnologia | InHire |
| [OLX Brasil](https://vemsergrupoolx.gupy.io) | Serviços e Outros | Gupy |
| [Omie](https://carreirasomie.gupy.io) | Tecnologia | Gupy |
| [Oncoclínicas](https://oncoclinicas.gupy.io) | Saúde | Gupy |
| [ONR – Registro de Imóveis Eletrônico](https://jobs.quickin.io/registradores/jobs) | Serviços e Outros | Quickin |
| [Open Co](https://carreiras.gupy.io/openco) | Financeiro | Gupy |
| [Oracle](https://www.oracle.com/careers) | Tecnologia | Site da Empresa |
| [Órama Investimentos](https://orama.gupy.io) | Serviços e Outros | Gupy |
| [Orizon](https://orizon.gupy.io) | Serviços e Outros | Gupy |
| [Outback (Bloomin Brands)](https://carreiras.gupy.io/bloominbrands) | Serviços e Outros | Gupy |
| [OXXO](https://oxxo.eightfold.ai/careers) | Serviços e Outros | Eightfold |
| [OYO Rooms](https://www.oyorooms.com/careers) | Serviços e Outros | Site da Empresa |
| [P&G](https://www.pgcareers.com/br/en) | Serviços e Outros | Workday |
| [Pacaembu Construtora](https://pacaembu.gupy.io) | Construção e Imóveis | Gupy |
| [Pagaleve](https://pagaleve.gupy.io) | Financeiro | Gupy |
| [Pagar.me](https://pagarme.gupy.io) | Financeiro | Gupy |
| [PagBank](https://carreiras.gupy.io/pagbank) | Financeiro | Gupy |
| [PagBank (PagSeguro)](https://pagbank.greenhouse.io) | Financeiro | Vagas |
| [PagSeguro](https://pagseguro.gupy.io) | Financeiro | Gupy |
| [Pague Menos](https://paguemenos.gupy.io) | Serviços e Outros | Gupy |
| [Panvel (Dimed)](https://panvel.gupy.io) | Serviços e Outros | Gupy |
| [Paramount](https://careers.paramount.com) | Serviços e Outros | Workday |
| [Paraná Banco](https://jobs.quickin.io/paranabanco/jobs) | Financeiro | Quickin |
| [Paschoalotto](https://paschoalotto.gupy.io) | Serviços e Outros | Gupy |
| [Passbolt](https://passbolt.inhire.com.br) | Tecnologia | InHire |
| [Payclip](https://payclip.bamboohr.com/careers) | Financeiro | Plataforma Interna |
| [Paypal](https://paypal.eightfold.ai/careers) | Financeiro | Eightfold |
| [PepsiCo](https://www.pepsicojobs.com/main) | Serviços e Outros | Kenexa |
| [Pernambucanas](https://vemprafamilia-pernambucanas.cliqx.com.br) | Serviços e Outros | CLIQQ |
| [Petlove](https://petlove.jobs.recrut.ai) | Serviços e Outros | Recrut.ai |
| [Petrobahia](https://petrobahia.gupy.io) | Energia e Utilities | Gupy |
| [Petrobras](https://petrobras.com.br/pt/quem-somos/carreiras) | Energia e Utilities | Site da Empresa |
| [Petz](https://petz.gupy.io) | Serviços e Outros | Gupy |
| [Pfizer](https://pfizer.wd1.myworkdayjobs.com/PfizerCareers) | Saúde | Workday |
| [PicPay](https://boards.greenhouse.io/picpay) | Financeiro | Greenhouse |
| [Pipefy](https://app.pipefy.com/organizations/28/interfaces/445e5dd7-d23f-4299-8777-9280272d015d/pages/83bf9609-eb1c-4f7c-8103-c6cc2170aeb0) | Tecnologia | Plataforma Interna |
| [Piracanjuba (Laticínios Bela Vista)](https://piracanjuba.gupy.io) | Serviços e Outros | Gupy |
| [Pismo](https://pismo.gupy.io) | Serviços e Outros | Gupy |
| [Plano & Plano](https://planoeplano.gupy.io) | Serviços e Outros | Gupy |
| [Platlog](https://platlog.gupy.io) | Serviços e Outros | Gupy |
| [PlayDelivery](https://playdelivery.gupy.io) | Logística e Mobilidade | Gupy |
| [Pleo](https://boards.greenhouse.io/pleo) | Financeiro | Greenhouse |
| [Polishop](https://polishop.gupy.io) | Serviços e Outros | Gupy |
| [Porto](https://porto.gupy.io) | Financeiro | Gupy |
| [Positive Brands](https://positivebrands.gupy.io) | Serviços e Outros | Gupy |
| [Positivo Tecnologia](https://positivo.gupy.io) | Serviços e Outros | Gupy |
| [Pottencial Seguradora](https://pottencial.gupy.io) | Financeiro | Gupy |
| [Pravaler](https://pravaler.gupy.io) | Indústria | Gupy |
| [PremieRpet](https://premierpet.gupy.io) | Serviços e Outros | Gupy |
| [Prevent Senior](https://www.preventsenior.com.br/trabalhe-conosco) | Saúde | Site da Empresa |
| [Prio](https://prio.gupy.io) | Serviços e Outros | Gupy |
| [Prosegur Brasil](https://prosegur.gupy.io) | Serviços e Outros | Gupy |
| [Protege](https://protege.gupy.io) | Serviços e Outros | Gupy |
| [Proton](https://job-boards.eu.greenhouse.io/proton) | Tecnologia | Greenhouse |
| [PUC-SP](https://pucsp.gupy.io) | Educação | Gupy |
| [PwC Global](https://pwc.wd3.myworkdayjobs.com/Global_Experienced_Careers) | Serviços e Outros | Workday |
| [PwC Portugal](https://pwcportugal.csod.com/ux/ats/careersite/4/home?c=pwcportugal) | Serviços e Outros | CSOD |
| [Qatar Airways](https://careers.qatarairways.com/global/en) | Serviços e Outros | Site da Empresa |
| [QCA](https://qca.gupy.io) | Serviços e Outros | Gupy |
| [QI Tech](https://qitech.inhire.app) | Financeiro | InHire |
| [Qlik](https://www.qlik.com/us/company/careers) | Tecnologia | Site da Empresa |
| [Qualicorp](https://qualicorp.gupy.io) | Serviços e Outros | Gupy |
| [Qualidados Engenharia](https://qualidados.gupy.io) | Serviços e Outros | Gupy |
| [Queiroz Galvão](https://queirozgalvao.gupy.io) | Serviços e Outros | Gupy |
| [Quinto Andar](https://job-boards.greenhouse.io/quintoandar) | Serviços e Outros | Greenhouse |
| [QuintoAndar](https://boards.greenhouse.io/quintoandar) | Tecnologia | Greenhouse |
| [QUOD](https://vempraquod.gupy.io) | Financeiro | Gupy |
| [Rabobank](https://www.rabobank.com/careers) | Financeiro | Workday |
| [Raizen](https://genteraizen.gupy.io) | Serviços e Outros | Gupy |
| [Raízs](https://raizs.gupy.io) | Serviços e Outros | Gupy |
| [Randon](https://randon.gupy.io) | Indústria | Gupy |
| [Rapiddo](https://rapiddo.gupy.io) | Serviços e Outros | Gupy |
| [Rappi](https://rappi.wd12.myworkdayjobs.com/es/Rappi_jobs) | Serviços e Outros | Workday |
| [Razer](https://razer.wd3.myworkdayjobs.com/Careers) | Serviços e Outros | Workday |
| [RBS](https://gruporbs.gupy.io) | Serviços e Outros | Gupy |
| [RD Saúde Corporativo](https://rdsaude-corporativo.gupy.io) | Saúde | Gupy |
| [RD Station](https://boards.greenhouse.io/rdstation) | Tecnologia | Greenhouse |
| [Real Expresso](https://realexpresso.gupy.io) | Serviços e Outros | Gupy |
| [Rebel](https://rebel.gupy.io) | Serviços e Outros | Gupy |
| [RecargaPay](https://apply.workable.com/recargapay) | Tecnologia | Workable |
| [Record](https://recordtv.gupy.io) | Serviços e Outros | Gupy |
| [Red Bull](https://jobs.redbull.com/br-pt) | Serviços e Outros | Plataforma Interna |
| [Red House International School](https://redhouse.gupy.io) | Educação | Gupy |
| [Rede](https://vemprarede.gupy.io) | Financeiro | Gupy |
| [Rede D Or](https://rededor.gupy.io) | Saúde | Gupy |
| [Rede DOr São Luiz](https://www.vagas.com.br/vagas-de-rededor) | Saúde | Vagas |
| [Redepharma Brasil](https://redepharma.gupy.io) | Serviços e Outros | Gupy |
| [Remotecom](https://job-boards.greenhouse.io/remotecom) | Tecnologia | Greenhouse |
| [Renner Lojas Br](https://renner.gupy.io) | Varejo e Consumo | Gupy |
| [Reserva](https://reserva.gupy.io) | Serviços e Outros | Gupy |
| [Riachuelo](https://riachuelo.gupy.io) | Serviços e Outros | Gupy |
| [Riot Games](https://www.riotgames.com/pt-br/trabalhe-conosco#job-list) | Mídia e Entretenimento | Plataforma Interna |
| [Rippling](https://ats.rippling.com/careers-quartile/jobs) | Tecnologia | Plataforma Interna |
| [Roche](https://roche.wd3.myworkdayjobs.com/roche-ext) | Saúde | Workday |
| [Rockstar Games](https://www.rockstargames.com/careers/openings) | Mídia e Entretenimento | Plataforma Interna |
| [Roldão Atacadista](https://roldao.gupy.io) | Agro e Alimentos | Gupy |
| [Romi](https://romi.gupy.io) | Serviços e Outros | Gupy |
| [Rossi Residencial](https://rossiresidencial.gupy.io) | Serviços e Outros | Gupy |
| [RTE Rodonaves](https://rodonaves.gupy.io) | Serviços e Outros | Gupy |
| [Rumo](https://rumo.empregare.com/pt-br) | Serviços e Outros | Gupy |
| [Rumo Logística](https://rumolog.gupy.io) | Logística e Mobilidade | Gupy |
| [Ryanair](https://careers.ryanair.com/jobs) | Serviços e Outros | Plataforma Interna |
| [Sabesp](https://carreiras.gupy.io/sabesp) | Serviços e Outros | Gupy |
| [Safra](https://venhasersafra.gupy.io) | Financeiro | Gupy |
| [Salesforce](https://www.salesforce.com/company/careers) | Tecnologia | Site da Empresa |
| [Sami](https://oisami.gupy.io) | Saúde | Gupy |
| [Samsung](https://sec.wd3.myworkdayjobs.com/Samsung_Careers) | Serviços e Outros | Workday |
| [Saneago](https://www.saneago.com.br/concursos) | Serviços e Outros | Vagas |
| [Sanepar](https://site.sanepar.com.br/trabalhe-com-a-gente) | Serviços e Outros | Vagas |
| [Sanofi](https://sanofi.wd3.myworkdayjobs.com/SanofiCareers) | Saúde | Workday |
| [Santa Casa BH](https://santacasabh.gupy.io) | Saúde | Gupy |
| [Santa Casa da Bahia](https://santacasaba.gupy.io) | Saúde | Gupy |
| [Santa Maria Ind](https://santamaria.gupy.io) | Serviços e Outros | Gupy |
| [Santander](https://www.santander.com.br/hotsite/carreiras) | Financeiro | SuccessFactors |
| [Santander Brasil](https://santander.gupy.io) | Serviços e Outros | Gupy |
| [Santos Brasil](https://santosbrasil.gupy.io) | Serviços e Outros | Gupy |
| [São Martinho](https://saomartinho.gupy.io) | Serviços e Outros | Gupy |
| [SAP](https://jobs.sap.com) | Tecnologia | Site da Empresa |
| [Savegnago](https://savegnago.recrut.ai) | Serviços e Outros | Vagas |
| [SBT](https://carreiras.gupy.io/sbt) | Serviços e Outros | Gupy |
| [Scania Latin America](https://scania.gupy.io) | Serviços e Outros | Gupy |
| [Schulz](https://schulz.gupy.io) | Serviços e Outros | Gupy |
| [Sebrae](https://sebrae.com.br) | Serviços e Outros | Manual |
| [Sem Parar](https://semparar.gupy.io) | Tecnologia | Gupy |
| [Semantix](https://jobs.quickin.io/semantix/jobs) | Tecnologia | Quickin |
| [Senac](https://www.senac.br) | Educação | Manual |
| [Senior Sistemas](https://carreiras.gupy.io/senior) | Tecnologia | Gupy |
| [Sensor Tower](https://jobs.lever.co/sensortower) | Tecnologia | Lever |
| [Ser Educacional](https://sereducacional.gupy.io) | Educação | Gupy |
| [Serasa Experian](https://careers.smartrecruiters.com/experian) | Tecnologia | SmartRecruiters |
| [Shape Digital](https://shapedigital.inhire.app/vagas) | Tecnologia | InHire |
| [Shell](https://carreiras.gupy.io/shell) | Serviços e Outros | Gupy |
| [Shipp](https://shipp.gupy.io) | Serviços e Outros | Gupy |
| [Shopee](https://careers.shopee.com.br/jobs) | Serviços e Outros | Plataforma Interna |
| [Shoulder](https://shoulder.gupy.io) | Serviços e Outros | Gupy |
| [Sicredi](https://sicredi.gupy.io) | Financeiro | Gupy |
| [Siemens](https://carreiras.gupy.io/siemens) | Indústria | Gupy |
| [Siemens Healthineers](https://carreiras.gupy.io/siemens-healthineers) | Saúde | Gupy |
| [Simpar](https://simpar.gupy.io) | Serviços e Outros | Gupy |
| [Sinch](https://apply.workable.com/sinch) | Tecnologia | Workable |
| [Singapore Airlines](https://www.singaporeair.com/en_UK/sg/careers) | Serviços e Outros | Site da Empresa |
| [Sirio-Libanes](https://www.hospitalsiriolibanes.org.br/trabalhe-conosco) | Saúde | Manual |
| [SLC Agrícola](https://slcagricola.gupy.io) | Serviços e Outros | Gupy |
| [Smart Fit](https://smartfit.gupy.io) | Serviços e Outros | Gupy |
| [Smart Kitchens](https://smartkitchens.gupy.io) | Serviços e Outros | Gupy |
| [Sode](https://sode.gupy.io) | Serviços e Outros | Gupy |
| [Sodexo](https://sodexobeneficios.gupy.io) | Serviços e Outros | Gupy |
| [Sodexo (Pluxee Brasil)](https://pluxee.gupy.io) | Serviços e Outros | Gupy |
| [Softplan](https://softplan.gupy.io) | Tecnologia | Gupy |
| [Solar Coca-Cola](https://solarcocacola.gupy.io) | Serviços e Outros | Gupy |
| [Sólides](https://vagas.solides.com.br) | Tecnologia | Sólides |
| [SONDA](https://career8.successfactors.com/career?company=SONDAP) | Tecnologia | SAP SuccessFactors |
| [Sony Global](https://sonyglobal.wd1.myworkdayjobs.com/en-US/SonyGlobalCareers) | Serviços e Outros | Workday |
| [Sony Interactive Entertainment Global](https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal) | Financeiro | Greenhouse |
| [Sony Music](https://boards.greenhouse.io/sonymusicentertainment) | Serviços e Outros | Gupy |
| [Sopra Steria](https://careers.soprasteria.co.uk/uk/en/job-search) | Serviços e Outros | Plataforma Interna |
| [Sourcegraph](https://boards.greenhouse.io/sourcegraph91) | Tecnologia | Greenhouse |
| [Spani Atacadista Var](https://spani.gupy.io) | Agro e Alimentos | Gupy |
| [SPDM Hospital São Paulo](https://spdm.gupy.io) | Saúde | Gupy |
| [Speedbird Aero](https://speedbird.gupy.io) | Serviços e Outros | Gupy |
| [Spotify](https://www.lifeatspotify.com) | Serviços e Outros | Site da Empresa |
| [Spread](https://spread.gupy.io) | Tecnologia | Gupy |
| [Stark Bank](https://stark.gupy.io) | Financeiro | Gupy |
| [Stefanini](https://stefanini.gupy.io) | Tecnologia | Gupy |
| [Stellantis](https://careers.stellantis.com) | Indústria | SuccessFactors |
| [Stone](https://stone.gupy.io) | Financeiro | Gupy |
| [Super Nosso](https://supernosso.recrut.ai) | Serviços e Outros | Recrut.ai |
| [Superdigital](https://superdigital.gupy.io) | Tecnologia | Gupy |
| [Supermercados BH](https://supermercadosbh.gupy.io) | Agro e Alimentos | Gupy |
| [Supermercados Guanabara](https://supermercadosguanabara.gupy.io) | Agro e Alimentos | Gupy |
| [Supportiv](https://supportiv.bamboohr.com/careers) | Saúde | BambooHR |
| [Suzano](https://suzano.gupy.io) | Indústria | Gupy |
| [Swap](https://swap.gupy.io) | Serviços e Outros | Gupy |
| [Swift](https://swift.gupy.io) | Serviços e Outros | Gupy |
| [Swile](https://jobs.lever.co/swile) | Tecnologia | Lever |
| [Swile Brasil](https://swile.workable.com) | Serviços e Outros | Vagas |
| [Sympla](https://sympla.inhire.app/vagas) | Tecnologia | InHire |
| [Syn Prop & Tech](https://syn.gupy.io) | Tecnologia | Gupy |
| [T-Systems Brasil](https://www.t-systems.com/br/pt/carreiras) | Tecnologia | Portal |
| [T4F - Time for Fun](https://t4f.vagas.solides.com.br) | Serviços e Outros | Solides |
| [Taco](https://taco.gupy.io) | Serviços e Outros | Gupy |
| [Taesa](https://taesa.gupy.io) | Serviços e Outros | Gupy |
| [Tahto Atendimento](https://tahto.gupy.io) | Serviços e Outros | Gupy |
| [TakeBlip](https://job-boards.greenhouse.io/blip-global) | Tecnologia | Greenhouse |
| [Team Liquid](https://careers.teamliquid.com/#jobs) | Serviços e Outros | Plataforma Interna |
| [Tecnisa](https://tecnisa.gupy.io) | Serviços e Outros | Gupy |
| [Tegma](https://tegma.gupy.io) | Serviços e Outros | Gupy |
| [Telefônica Brasil (Vivo)](https://vivo.gupy.io) | Energia e Utilities | Gupy |
| [Telhanorte](https://www.vagas.com.br/vagas-de-telhanorte) | Serviços e Outros | Vagas |
| [Telus Digital BR](https://telusdigital.com/careers) | Tecnologia | Greenhouse |
| [Tembici](https://carreiras.gupy.io/tembici) | Serviços e Outros | Gupy |
| [Tenda](https://tenda.gupy.io) | Serviços e Outros | Gupy |
| [Terra Santa](https://terrasanta.gupy.io) | Serviços e Outros | Gupy |
| [The New](https://thenew.gupy.io) | Serviços e Outros | Gupy |
| [ThoughtWorks](https://www.thoughtworks.com/careers/jobs) | Tecnologia | Plataforma Interna |
| [Ticket (Edenred Brasil)](https://edenred.gupy.io) | Serviços e Outros | Gupy |
| [Tigre](https://tigre.gupy.io) | Serviços e Outros | Gupy |
| [TIM Brasil](https://tim.gupy.io) | Energia e Utilities | Gupy |
| [TIVIT](https://talent.gupy.io/tivit) | Tecnologia | Gupy |
| [Tok&Stok](https://tokstok.pandape.infojobs.com.br) | Serviços e Outros | InfoJobs |
| [Tokio Marine](https://tokiomarine.gupy.io) | Financeiro | Gupy |
| [Total Express](https://totalexpress.gupy.io) | Serviços e Outros | Gupy |
| [Totvs](https://carreiras.gupy.io/totvs) | Tecnologia | Gupy |
| [Toyota](https://carreiras.gupy.io/toyota) | Indústria | Gupy |
| [Toyota Brasil](https://toyota.wd503.myworkdayjobs.com/pt-BR/TLAC) | Indústria | Workday |
| [Track&Field](https://tfcarreira.gupy.io) | Serviços e Outros | Gupy |
| [Tractian](https://careers.tractian.com/jobs) | Serviços e Outros | Plataforma Interna |
| [Tramontina](https://tramontina.gupy.io) | Serviços e Outros | Gupy |
| [Transperfect Gaming](https://gaming.transperfect.com/careers) | Serviços e Outros | Plataforma Interna |
| [Transport NSW](https://jobs.transport.nsw.gov.au/search) | Serviços e Outros | Plataforma Interna |
| [TranspoTech](https://transpotech.gupy.io) | Tecnologia | Gupy |
| [TransUnion](https://transunion.wd5.myworkdayjobs.com/TransUnion) | Financeiro | Workday |
| [Traz Pra Mim](https://trazpramim.gupy.io) | Serviços e Outros | Gupy |
| [Trigg](https://trigg.gupy.io) | Serviços e Outros | Gupy |
| [Trisul](https://trisul.gupy.io) | Serviços e Outros | Gupy |
| [Triunfo Participações](https://triunfo.gupy.io) | Serviços e Outros | Gupy |
| [TruckPad](https://truckpad.gupy.io) | Serviços e Outros | Gupy |
| [Trybe](https://betrybe.inhire.app/vagas) | Tecnologia | InHire |
| [Tupy](https://tupy.gupy.io) | Indústria | Gupy |
| [Uber Brasil](https://www.uber.com/br/pt/careers) | Serviços e Outros | Portal |
| [Ubisoft](https://www.ubisoft.com/en-us/company/careers) | Serviços e Outros | Site da Empresa |
| [Uello](https://uello.gupy.io) | Serviços e Outros | Gupy |
| [Ultrapar](https://ultrapar.gupy.io) | Serviços e Outros | Gupy |
| [União Química](https://uniaoquimica.gupy.io) | Serviços e Outros | Gupy |
| [Unico](https://unicotech.inhire.app/vagas) | Tecnologia | InHire |
| [Unicred](https://unicred.gupy.io) | Financeiro | Gupy |
| [Unidas](https://unidas.gupy.io) | Serviços e Outros | Gupy |
| [Unifique](https://vemserunifique.gupy.io) | Serviços e Outros | Gupy |
| [Unilever](https://careers.unilever.com/en/search-jobs) | Serviços e Outros | Workday |
| [Unimed (Sistema Nacional)](https://unimednacional.gupy.io) | Saúde | Gupy |
| [Unimed Belém Oficial](https://unimedbelem.gupy.io) | Saúde | Gupy |
| [Unimed Brasil](https://unimed-brasil.gupy.io) | Saúde | Gupy |
| [Unimed Campina Grande Oficial](https://unimedcampinagrande.gupy.io) | Saúde | Gupy |
| [Unimed Campinas Oficial](https://unimedcampinas.gupy.io) | Saúde | Gupy |
| [Unimed Cuiabá Oficial](https://unimedcuiaba.gupy.io) | Saúde | Gupy |
| [Unimed Fortaleza](https://unimedfortaleza.gupy.io) | Saúde | Gupy |
| [Unimed Goiânia Oficial](https://unimedgoiania.gupy.io) | Saúde | Gupy |
| [Unimed Maceió Oficial](https://unimedmaceio.gupy.io) | Saúde | Gupy |
| [Unimed Piracicaba Oficial](https://unimedpiracicaba.gupy.io) | Saúde | Gupy |
| [Unimed Porto Alegre](https://unimedpoa.gupy.io) | Saúde | Gupy |
| [Unimed Teresina Oficial](https://unimedteresina.gupy.io) | Saúde | Gupy |
| [Unipar Carbocloro](https://unipar.gupy.io) | Educação | Gupy |
| [United Airlines](https://careers.united.com) | Serviços e Outros | Site da Empresa |
| [UOL Brasil Br](https://uol.gupy.io) | Serviços e Outros | Gupy |
| [UOL Compass](https://compass.gupy.io) | Serviços e Outros | Gupy |
| [UP Brasil](https://upbrasil.pandape.infojobs.com.br) | Financeiro | InfoJobs |
| [Usiminas](https://usiminas.gupy.io) | Indústria | Gupy |
| [Usina Alta Mogiana](https://altamogiana.gupy.io) | Serviços e Outros | Gupy |
| [V.tal](https://vtal.gupy.io) | Serviços e Outros | Gupy |
| [Vagas.com](https://vagas.gupy.io) | Tecnologia | Gupy |
| [Vale](https://carreiras.gupy.io/vale) | Indústria | Gupy |
| [Valid](https://valid.gupy.io) | Tecnologia | Gupy |
| [Vamos](https://vamos.gupy.io) | Serviços e Outros | Gupy |
| [Vasta Educação](https://vastaeducacao.gupy.io) | Educação | Gupy |
| [Veeva](https://veeva.com/careers) | Tecnologia | Lever |
| [Veirano Advogados](https://veirano.gupy.io) | Serviços e Outros | Gupy |
| [Veloe](https://vagas.veloe.com.br/jobs) | Financeiro | Bizneo |
| [Verde Campo](https://verdecampo.gupy.io) | Serviços e Outros | Gupy |
| [Via Varejo](https://viavarejo.gupy.io) | Varejo e Consumo | Gupy |
| [Viacredi](https://viacredi.gupy.io) | Serviços e Outros | Gupy |
| [Vibra Energia](https://vibraenergia.gupy.io) | Energia e Utilities | Gupy |
| [Vibra Energia Brasil Br](https://vibra.gupy.io) | Energia e Utilities | Gupy |
| [Vila Nova Log](https://vilanova.gupy.io) | Serviços e Outros | Gupy |
| [Villela Brasil Bank](https://villelabrasilbank.gupy.io) | Financeiro | Gupy |
| [Vindi](https://vindi.gupy.io) | Financeiro | Gupy |
| [Vinta](https://vinta.inhire.app/vagas) | Tecnologia | InHire |
| [Visa](https://carreiras.gupy.io/visa) | Financeiro | Gupy |
| [Vitru](https://vitru.gupy.io) | Serviços e Outros | Gupy |
| [Vivara](https://vivara.gupy.io) | Serviços e Outros | Gupy |
| [Viver](https://viver.gupy.io) | Serviços e Outros | Gupy |
| [Vivo Digital](https://vivodigital.gupy.io) | Energia e Utilities | Gupy |
| [VLI Logística](https://vli.gupy.io) | Logística e Mobilidade | Gupy |
| [Volkswagen](https://carreiras.gupy.io/volkswagen) | Indústria | Gupy |
| [Volkswagen do Brasil](https://vwbrasil.gupy.io) | Indústria | Gupy |
| [Volvo](https://www.volvogroup.com/en/careers.html) | Indústria | Site da Empresa |
| [Volvo Infor](https://career55.sapsf.eu/careers?company=volvoinfor) | Indústria | SAP SuccessFactors |
| [Votorantim Cimentos](https://votorantimcimentos.gupy.io) | Indústria | Gupy |
| [Votorantim S.A.](https://votorantim.gupy.io) | Financeiro | Gupy |
| [VR](https://www.portalsinergyrh.com.br/Portal/MeuPortal/MeuPortal?empresa=1581&master=0#suaNovoCarreira) | Financeiro | Plataforma Interna |
| [VR Benefícios](https://vr.gupy.io) | Serviços e Outros | Gupy |
| [VTEX](https://job-boards.greenhouse.io/vtex) | Tecnologia | Greenhouse |
| [Vulcabras](https://vulcabras.gupy.io) | Indústria | Gupy |
| [Warner Bros. Discovery](https://careers.wbd.com/hbo-jobs) | Serviços e Outros | Plataforma Interna |
| [Warren](https://warren.gupy.io) | Serviços e Outros | Gupy |
| [webedia](https://webedia.gupy.io) | Serviços e Outros | Gupy |
| [Webmotors](https://webmotors.gupy.io) | Indústria | Gupy |
| [WEG](https://weg.gupy.io) | Indústria | Gupy |
| [Wellhub (GymPass)](https://boards.greenhouse.io/gympass) | Saúde | Greenhouse |
| [Welocalize](https://jobs.lever.co/welocalize) | Serviços e Outros | Lever |
| [Westwing](https://westwing.gupy.io) | Serviços e Outros | Gupy |
| [WeWork](https://wework.wd1.myworkdayjobs.com/WeWork) | Serviços e Outros | Workday |
| [WEX](https://wexinc.wd5.myworkdayjobs.com/WEXInc) | Financeiro | Workday |
| [Wildlife Studios](https://boards.greenhouse.io/wildlifestudios) | Serviços e Outros | Greenhouse |
| [Wilhelmsen](https://wilhelmsen.wd3.myworkdayjobs.com/Wilhelmsen) | Serviços e Outros | Workday |
| [will bank](https://willbank.inhire.app/vagas) | Financeiro | InHire |
| [WillowTree](https://willowtreeapps.com/careers) | Tecnologia | Greenhouse |
| [Wilson Sons](https://wilsonsons.gupy.io) | Serviços e Outros | Gupy |
| [Wiz Co](https://wiz.gupy.io) | Financeiro | Gupy |
| [Wordpress-proxy](https://wordpress-proxy.inhire.com.br) | Tecnologia | InHire |
| [Xometry](https://job-boards.greenhouse.io/xometry) | Tecnologia | Greenhouse |
| [XP Banco](https://xpinvestimentos.gupy.io) | Financeiro | Gupy |
| [XP Inc](https://boards.greenhouse.io/xpinc) | Financeiro | Greenhouse |
| [Yamaha](https://yamaha.gupy.io) | Indústria | Gupy |
| [Yduqs](https://yduqs.gupy.io) | Educação | Gupy |
| [Yorgus](https://yorgus.gupy.io) | Serviços e Outros | Gupy |
| [Youse](https://vagas-youse.gupy.io) | Financeiro | Gupy |
| [Zaffari](https://zaffari.gupy.io) | Serviços e Outros | Gupy |
| [Zé Delivery](https://carreiras.gupy.io/zedelivery) | Logística e Mobilidade | Gupy |
| [Zendesk](https://www.zendesk.com.br/company/careers) | Tecnologia | Site da Empresa |
| [Zenir](https://zenir.gupy.io) | Serviços e Outros | Gupy |
| [ZF Friedrich](https://career5.successfactors.eu/careers?company=zffriedric) | Indústria | SAP SuccessFactors |
| [Zoom](https://careers.zoom.us/home) | Tecnologia | Site da Empresa |
| [Zup Innovation](https://job-boards.greenhouse.io/zupinnovation) | Tecnologia | Greenhouse |
