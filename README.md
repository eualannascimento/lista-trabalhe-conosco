## 📚 Introdução
O objetivo deste repositório é facilitar o acesso e a busca por oportunidades de trabalho em diferentes empresas, centralizando as plataformas em um só lugar.  
Sinta-se à vontade para contribuir adicionando ou atualizando a lista de empresas.  
Este repositório contém uma lista com: 
- Data de Entrada (ou seja, quando entrou na lista);
- Nome da Empresa;
- Segmento da Empresa;
- Plataforma para processo seletivo;
- Link para acesso ao site;
- Data do Status (Última data em que o link foi verificado);
- Status da URL (Se o link está ativo ou não).
<br><br>  
## 🔧 Processo
O processo de atualização do README.md para acesso rápido é automatizado por meio do GitHub Actions.  
- O fluxo de trabalho 'update-readme.yml', é executado sempre que houver um push na branch main.  
- Este fluxo de trabalho executa o update-readme.py, que lê o arquivo 'src/md/header.md' e o 'src/csv/career-websites.csv', ordena os dados por data de referência e escreve o arquivo README.md com as informações atualizadas.
- Além desse fluxo de trabalho, temos o 'verify-websites.yml', que é executado uma vez por semana, ele verifica se o site está funcionando (através de algumas requisições) e faz a marcação do status no 'src/csv/career-websites.csv'.
<br><br>
## 🤝 Como contribuir
1. Faça um fork do repositório do projeto;
2. Abra o arquivo 'src/csv/career-websites.csv' e faça suas contribuições (adicionando ou editando);
3. Salve o arquivo 'src/csv/career-websites.csv' com as alterações.
4. Faça o commit e o push para o seu repositório forkado.
5. Abra um pull request (PR) para o repositório original do projeto, especificando que deseja adicionar ou editar empresas.
6. Aguarde a revisão do PR (possíveis solicitações de alteração) e a eventual aprovação e merge.
<br><br>
## 🏢 Acesso rápido
Para obter todas as informações disponíveis, basta baixar o arquivo 'src/csv/career-websites.csv'.  
Essa tabela contém somente o nome da empresa com link para o site, visando facilitar o uso via mobile.
<br>

| Nome da Empresa (+ Link do Trabalhe Conosco) | Segmento | Última Vaga |
| --- | --- | --- |
| [77sol](https://77sol.gupy.io) | A Classificar | 2026-02-20 |
| [Algar Tech Br](https://algar.gupy.io) | Telecom | 2026-02-20 |
| [Alloha Fibra](https://allohafibra.gupy.io) | Telecom | 2026-02-20 |
| [CCR](https://motiva.gupy.io) | Infraestrutura | 2026-02-20 |
| [Franq](https://franq.gupy.io) | Fintech | 2026-02-20 |
| [Grupo L'Occitane](https://sejaloccitane.gupy.io) | Cosméticos | 2026-02-20 |
| [Grupo Marilan](https://marilan.gupy.io) | Alimentos | 2026-02-20 |
| [JHSF](https://jhsf.gupy.io) | Construção | 2026-02-20 |
| [Mobit Tecnologia](https://mobit.gupy.io) | Estratégico | 2026-02-20 |
| [Mutant](https://mutantbrvagas.gupy.io) | Tecnologia | 2026-02-20 |
| [Qualidados Engenharia](https://qualidados.gupy.io) | Estratégico | 2026-02-20 |
| [Sicredi](https://sicredi.gupy.io) | Cooperativa | 2026-02-20 |
| [Tegma](https://tegma.gupy.io) | Estratégico | 2026-02-20 |
| [Unimed Maceió Oficial](https://unimedmaceio.gupy.io) | Saúde | 2026-02-20 |
| [Volkswagen do Brasil](https://vwbrasil.gupy.io) | Automotivo | 2026-02-20 |
| [3cservices](https://3cservices.gupy.io) | A Classificar | 2026-02-19 |
| [Abakids](https://abakids.gupy.io) | A Classificar | 2026-02-19 |
| [ANBIMA](https://anbima.gupy.io) | Entidade Financeira | 2026-02-19 |
| [Bauducco](https://bauducco.gupy.io) | Alimentos e Bebidas | 2026-02-19 |
| [CBA Alumínio](https://cba.gupy.io) | Indústria | 2026-02-19 |
| [Cocamar](https://cocamar.gupy.io) | Agronegócio | 2026-02-19 |
| [Creditas](https://creditas.gupy.io) | Financeiro | 2026-02-19 |
| [Energisa (Corp)](https://grupoenergisa.gupy.io) | Energia | 2026-02-19 |
| [iPlace](https://iplace.gupy.io) | Varejo | 2026-02-19 |
| [McDonalds (Corporativo)](https://corporativomc.gupy.io) | Restaurante | 2026-02-19 |
| [Mercedes-Benz Caminhões & Ônibus (Externa)](https://mercedes-benzcaminhoeseonibus.gupy.io) | Automotivo | 2026-02-19 |
| [Mondelez Brasil](https://mondelez.gupy.io) | Alimentos | 2026-02-19 |
| [Pagaleve](https://pagaleve.gupy.io) | Fintech | 2026-02-19 |
| [Softplan](https://softplan.gupy.io) | Tecnologia | 2026-02-19 |
| [Unimed Belém Oficial](https://unimedbelem.gupy.io) | Saúde | 2026-02-19 |
| [Agrária](https://agraria.gupy.io) | Estratégico | 2026-02-18 |
| [Brisanet](https://brisanet.gupy.io) | Telecom | 2026-02-18 |
| [Casa Di Conti](https://casadiconti.gupy.io) | Bebidas | 2026-02-18 |
| [CIEE SC](https://cieesc.gupy.io) | Serviços | 2026-02-18 |
| [Cinemark](https://cinemark.gupy.io) | Cultura | 2026-02-18 |
| [Cury](https://cury.gupy.io) | Construção | 2026-02-18 |
| [Fortlev](https://fortlev.gupy.io) | Indústria | 2026-02-18 |
| [Grupo Zaffari](https://grupozaffari.gupy.io) | Varejo | 2026-02-18 |
| [Hospital Care](https://hospitalcare.gupy.io) | Saúde | 2026-02-18 |
| [Randon Corp](https://randoncorp.gupy.io) | Indústria | 2026-02-18 |
| [Scania Latin America](https://scania.gupy.io) | Estratégico | 2026-02-18 |
| [Vivo](https://vivo.gupy.io) | Telecom | 2026-02-18 |
| [Cocal](https://cocal.gupy.io) | Agronegócio | 2026-02-17 |
| [Ecossistema ARGENTA](https://argenta.gupy.io) | Varejo | 2026-02-17 |
| [Marisol](https://marisol.gupy.io) | Moda | 2026-02-17 |
| [Votorantim Cimentos](https://votorantimcimentos.gupy.io) | Finanças/Banco & Fintech | 2026-02-17 |
| [Grupo Bertolini](https://bertolini.gupy.io) | Indústria | 2026-02-16 |
| [DASA Programas de Entrada](https://dasaprogramasdeentrada.gupy.io) | Saúde | 2026-02-14 |
| [ArcelorMittal Tuper Brasil](https://tuper.gupy.io) | Indústria | 2026-02-13 |
| [Assaí Atacadista](https://assai.gupy.io) | Varejo | 2026-02-13 |
| [Cosan](https://cosan.gupy.io) | Energia/Petróleo | 2026-02-13 |
| [Credcrea (Ailos)](https://credcrea.gupy.io) | Finanças | 2026-02-13 |
| [Fast Shop](https://fastshop.gupy.io) | Varejo | 2026-02-13 |
| [Sem Parar](https://semparar.gupy.io) | Tecnologia | 2026-02-13 |
| [Shoulder](https://shoulder.gupy.io) | Moda | 2026-02-13 |
| [Vivo Digital](https://vivodigital.gupy.io) | Telecom | 2026-02-13 |
| [3corptechnology](https://3corptechnology.gupy.io) | A Classificar | 2026-02-12 |
| [Alpargatas](https://alpargatas.gupy.io) | Indústria | 2026-02-12 |
| [Cencosud Brasil](https://cencosudbrasil.gupy.io) | Varejo | 2026-02-12 |
| [CVC Corp](https://cvccorp.gupy.io) | Turismo | 2026-02-12 |
| [DASA Tecnologia](https://dasatecnologia.gupy.io) | Saúde | 2026-02-12 |
| [Elgin](https://sejaelgin.gupy.io) | Eletrodomésticos | 2026-02-12 |
| [FSG Centro Universitário](https://fsg.gupy.io) | Educação | 2026-02-12 |
| [Itaú](https://vemproitau.gupy.io) | Banco | 2026-02-12 |
| [KMM](https://kmm.gupy.io) | Consultoria | 2026-02-12 |
| [Kovi](https://kovi.gupy.io) | Mobilidade | 2026-02-12 |
| [LG Electronics do Brasil LTDA](https://lge.gupy.io) | Eletrônicos | 2026-02-12 |
| [Piracanjuba (Laticínios Bela Vista)](https://piracanjuba.gupy.io) | Estratégico | 2026-02-12 |
| [Positivo Tecnologia](https://positivo.gupy.io) | Estratégico | 2026-02-12 |
| [Spread](https://spread.gupy.io) | Tecnologia | 2026-02-12 |
| [Syn Prop & Tech](https://syn.gupy.io) | Imobiliário | 2026-02-12 |
| [Tenda](https://tenda.gupy.io) | Construção | 2026-02-12 |
| [UOL Compass](https://compass.gupy.io) | Consultoria | 2026-02-12 |
| [Vila Nova Log](https://vilanova.gupy.io) | Logística | 2026-02-12 |
| [Beep Saúde](https://beepsaude.gupy.io) | Saúde | 2026-02-11 |
| [Caju](https://caju.gupy.io) | Benefícios | 2026-02-11 |
| [Copersucar](https://copersucar.gupy.io) | Agronegócio | 2026-02-11 |
| [Dotz](https://dotz.gupy.io) | Benefícios | 2026-02-11 |
| [Elo](https://vempraelo.gupy.io) | Soluções de Pagamento | 2026-02-11 |
| [Itaú Social](https://itausocial.gupy.io) | Estratégico | 2026-02-11 |
| [Redepharma Brasil](https://redepharma.gupy.io) | Varejo | 2026-02-11 |
| [Unimed Cuiabá Oficial](https://unimedcuiaba.gupy.io) | Saúde | 2026-02-11 |
| [Afya Educacional](https://afya.gupy.io) | Educação | 2026-02-10 |
| [Bemobi](https://bemobi.gupy.io) | Tecnologia | 2026-02-10 |
| [Bunge](https://bunge.gupy.io) | Indústria | 2026-02-10 |
| [Embraer](https://embraer.gupy.io) | Indústria | 2026-02-10 |
| [HBR Realty](https://hbrrealty.gupy.io) | Estratégico | 2026-02-10 |
| [Korp ERP](https://korp.gupy.io) | Tecnologia | 2026-02-10 |
| [Mills](https://mills.gupy.io) | Estratégico | 2026-02-10 |
| [Rumo Logística](https://rumolog.gupy.io) | Logística | 2026-02-10 |
| [Spani Atacadista Var](https://spani.gupy.io) | Varejo | 2026-02-10 |
| [Unimed Nacional](https://unimednacional.gupy.io) | Saúde | 2026-02-10 |
| [Digio](https://digio.gupy.io) | Finanças/Banco & Fintech | 2026-02-09 |
| [Grupo Boticário](https://grupoboticario.gupy.io) | Cosméticos | 2026-02-09 |
| [Henry Schein Brasil](https://henryschein.gupy.io) | Saúde | 2026-02-09 |
| [Multilog](https://multilog.gupy.io) | Logística | 2026-02-09 |
| [Santa Casa da Bahia](https://santacasaba.gupy.io) | Saúde | 2026-02-09 |
| [Stefanini](https://stefanini.gupy.io) | Tecnologia | 2026-02-09 |
| [Tigre](https://tigre.gupy.io) | Estratégico | 2026-02-09 |
| [ICI Curitiba](https://ici.gupy.io) | Tecnologia | 2026-02-08 |
| [Club Athletico Paranaense](https://athletico.gupy.io) | Esportes | 2026-02-06 |
| [Delivery Much](https://deliverymuch.gupy.io) | Estratégico | 2026-02-06 |
| [Fundação São Paulo (FUNDASP)](https://fundasp.gupy.io) | Educacional | 2026-02-06 |
| [Leve Saúde](https://levesaude.gupy.io) | Saúde | 2026-02-06 |
| [QCA](https://qca.gupy.io) | Serviços | 2026-02-06 |
| [Renner Lojas Br](https://renner.gupy.io) | Varejo | 2026-02-06 |
| [Safra](https://venhasersafra.gupy.io) | Finanças/Banco & Fintech | 2026-02-06 |
| [Unimed Campina Grande Oficial](https://unimedcampinagrande.gupy.io) | Saúde | 2026-02-06 |
| [Usina Alta Mogiana](https://altamogiana.gupy.io) | Estratégico | 2026-02-06 |
| [Abaco](https://abaco.gupy.io) | A Classificar | 2026-02-05 |
| [Coco Bambu](https://cocobambu.gupy.io) | Alimentos e Bebidas | 2026-02-05 |
| [Guanabara](https://guanabara.gupy.io) | Estratégico | 2026-02-05 |
| [Lojas Renner S.A.](https://encantech.gupy.io) | Varejo | 2026-02-05 |
| [Paschoalotto](https://paschoalotto.gupy.io) | Gestão de Relacionamentos | 2026-02-05 |
| [Positivo Tecnologia](https://positivotecnologia.gupy.io) | Estratégico | 2026-02-05 |
| [Supermercados Guanabara](https://supermercadosguanabara.gupy.io) | Varejo | 2026-02-05 |
| [Vibra Energia Brasil Br](https://vibra.gupy.io) | Energia/Petróleo | 2026-02-05 |
| [Banco Rodobens](https://rodobenscarreiras.gupy.io) | Finanças/Banco & Fintech | 2026-02-04 |
| [BrasilAgro](https://brasilagro.gupy.io) | Agronegócio | 2026-02-04 |
| [Brasilprev](https://brasilprev.gupy.io) | Seguradora | 2026-02-04 |
| [Castrolanda](https://castrolanda.gupy.io) | Agronegócio | 2026-02-04 |
| [Cimed](https://cimed.gupy.io) | Farmacêutica | 2026-02-04 |
| [Globo](https://globo.gupy.io) | Televisão | 2026-02-04 |
| [Hypera Pharma](https://hyperapharma.gupy.io) | Farmacêutica | 2026-02-04 |
| [Localiza](https://localiza.gupy.io) | Locação | 2026-02-04 |
| [Méliuz Brasil Tech](https://meliuz.gupy.io) | Tecnologia | 2026-02-04 |
| [OLX Brasil](https://vemsergrupoolx.gupy.io) | Marketplace | 2026-02-04 |
| [Randon](https://randon.gupy.io) | Indústria | 2026-02-04 |
| [Unicred](https://unicred.gupy.io) | Finanças | 2026-02-04 |
| [Banco Fibra](https://bancofibra.gupy.io) | Finanças/Banco & Fintech | 2026-02-03 |
| [Cris Barros](https://crisbarros.gupy.io) | Moda | 2026-02-03 |
| [DASA Assistencial](https://dasaassistencial.gupy.io) | Saúde | 2026-02-03 |
| [DASA Atendimento](https://dasaatendimento.gupy.io) | Saúde | 2026-02-03 |
| [DASA Diversidade](https://diversidasa.gupy.io) | Saúde | 2026-02-03 |
| [Genial Investimentos](https://genial.gupy.io) | Estratégico | 2026-02-03 |
| [UOL Brasil Br](https://uol.gupy.io) | Mídia | 2026-02-03 |
| [Vivara](https://vivara.gupy.io) | Varejo | 2026-02-03 |
| [Youse](https://vagas-youse.gupy.io) | Seguros | 2026-02-03 |
| [Americanas S.A.](https://americanas.gupy.io) | Varejo | 2026-02-02 |
| [Banco ABC](https://abcbrasil.gupy.io) | Finanças/Banco & Fintech | 2026-02-02 |
| [Caoa](https://caoa.gupy.io) | Automotivo | 2026-02-02 |
| [Cruzeiro do Sul](https://cruzeirodosul.gupy.io) | Educação | 2026-02-02 |
| [CSN](https://csn.gupy.io) | Siderurgia | 2026-02-02 |
| [DRUID Creative Gaming](https://druid.gupy.io) | Games | 2026-02-02 |
| [Intelipost](https://intelipost.gupy.io) | Estratégico | 2026-02-02 |
| [Record](https://recordtv.gupy.io) | Televisão | 2026-02-02 |
| [Tecnisa](https://tecnisa.gupy.io) | Estratégico | 2026-02-02 |
| [Valid](https://valid.gupy.io) | Tecnologia | 2026-02-02 |
| [Auren Energia](https://aurenenergia.gupy.io) | Energia | 2026-01-30 |
| [Azul](https://voeazul.gupy.io) | Aviação | 2026-01-30 |
| [Cristália](https://cristalia.gupy.io) | Farmacêutica | 2026-01-30 |
| [Centauro](https://centaurotalentos.gupy.io) | Varejo | 2026-01-29 |
| [Dexco](https://dexco.gupy.io) | Indústria | 2026-01-29 |
| [Gupy](https://vempra.gupy.io) | HRTech | 2026-01-29 |
| [Honda](https://honda.gupy.io) | Automotivo | 2026-01-29 |
| [JBS](https://grupojbs.gupy.io) | Alimentos e Bebidas | 2026-01-29 |
| [Petrobahia](https://petrobahia.gupy.io) | Estratégico | 2026-01-29 |
| [Suzano](https://suzano.gupy.io) | Indústria | 2026-01-29 |
| [Unimed Brasil](https://unimed-brasil.gupy.io) | Saúde | 2026-01-29 |
| [2comconsulting](https://2comconsulting.gupy.io) | A Classificar | 2026-01-28 |
| [A3consultoria](https://a3consultoria.gupy.io) | A Classificar | 2026-01-28 |
| [Aramis](https://aramis.gupy.io) | Moda | 2026-01-28 |
| [Condor Supermercados](https://condor.gupy.io) | Varejo | 2026-01-28 |
| [Cruzeiro do Sul Educacional](https://cruzeirodosuleducacional.gupy.io) | Educação | 2026-01-28 |
| [CVP (Caixa Vida e Previdência)](https://caixavidaeprevidencia.gupy.io) | Estratégico | 2026-01-28 |
| [Grupo Nós](https://gruponos.gupy.io) | Varejo | 2026-01-28 |
| [Hering](https://ciahering.gupy.io) | Varejo | 2026-01-28 |
| [M. Dias Branco](https://mdiasbranco.gupy.io) | Alimentos e Bebidas | 2026-01-28 |
| [Monte Carlo Moda](https://montecarlo.gupy.io) | Moda | 2026-01-28 |
| [RD Saúde Corporativo](https://rdsaude-corporativo.gupy.io) | Saúde | 2026-01-28 |
| [Unimed Piracicaba Oficial](https://unimedpiracicaba.gupy.io) | Saúde | 2026-01-28 |
| [C&A](https://cea.gupy.io) | Varejo | 2026-01-27 |
| [Decathlon](https://carreirasdecathlon.gupy.io) | Esportes | 2026-01-27 |
| [Farm Moda Br](https://farm.gupy.io) | Moda | 2026-01-27 |
| [Hering](https://hering.gupy.io) | Varejo | 2026-01-27 |
| [Prio](https://prio.gupy.io) | Energy | 2026-01-27 |
| [Aché](https://vagasache.gupy.io) | Farmacêutica | 2026-01-26 |
| [Casa e Video Varejo](https://casaevideo.gupy.io) | Varejo | 2026-01-26 |
| [PremieRpet](https://premierpet.gupy.io) | Alimentos | 2026-01-26 |
| [AgroGalaxy](https://agrogalaxy.gupy.io) | Agronegócio | 2026-01-23 |
| [Asaas](https://asaas.gupy.io) | Fintech | 2026-01-23 |
| [EZTEC](https://eztec.gupy.io) | Construção | 2026-01-23 |
| [Hospital Moinhos de Vento](https://hospitalmoinhos.gupy.io) | Saúde | 2026-01-23 |
| [Nazária](https://nazaria.gupy.io) | Estratégico | 2026-01-23 |
| [Viacredi](https://viacredi.gupy.io) | Estratégico | 2026-01-23 |
| [BMG](https://bmg.gupy.io) | Finanças/Banco & Fintech | 2026-01-22 |
| [Cacau Show](https://cacaushow.gupy.io) | Alimentos e Bebidas | 2026-01-22 |
| [DASA Corp](https://dasacorp.gupy.io) | Saúde | 2026-01-22 |
| [GPA](https://corporacaogpa.gupy.io) | Varejo | 2026-01-22 |
| [Orizon](https://orizon.gupy.io) | Estratégico | 2026-01-22 |
| [Tupy](https://tupy.gupy.io) | Indústria | 2026-01-22 |
| [Jequiti](https://jequiti.gupy.io) | Estratégico | 2026-01-21 |
| [Platlog](https://platlog.gupy.io) | Logística | 2026-01-21 |
| [Rede](https://vemprarede.gupy.io) | Soluções de Pagamento | 2026-01-21 |
| [Andorinha Supermercados](https://andorinha.gupy.io) | Varejo | 2026-01-20 |
| [BHS](https://bhs.gupy.io) | Tecnologia | 2026-01-20 |
| [Gupy Tech](https://tech-career.gupy.io) | HRTech | 2026-01-20 |
| [Helbor](https://helbor.gupy.io) | Estratégico | 2026-01-20 |
| [Livelo](https://livelo.gupy.io) | Recompensas | 2026-01-20 |
| [Swift](https://swift.gupy.io) | Alimentos e Bebidas | 2026-01-20 |
| [webedia](https://webedia.gupy.io) | Estratégico | 2026-01-20 |
| [Equatorial Energia](https://equatorialenergia.gupy.io) | Energia | 2026-01-19 |
| [QUOD](https://vempraquod.gupy.io) | Birô de Crédito | 2026-01-19 |
| [Animale Moda Br](https://animale.gupy.io) | Moda | 2026-01-16 |
| [Camicado (Lojas Renner)](https://lojasrenner.gupy.io) | Varejo | 2026-01-16 |
| [Dafiti Tech Br](https://dafiti.gupy.io) | Tecnologia | 2026-01-16 |
| [Enjoei](https://enjoei.gupy.io) | Varejo | 2026-01-16 |
| [KRYPTUS](https://kryptus.gupy.io) | Cibersegurança | 2026-01-16 |
| [Wilson Sons](https://wilsonsons.gupy.io) | Logística | 2026-01-16 |
| [Getnet](https://getnet.gupy.io) | Fintech | 2026-01-15 |
| [Tokio Marine](https://tokiomarine.gupy.io) | Finanças/Seguros | 2026-01-15 |
| [Itaú Cultural](https://itaucultural.gupy.io) | Banco | 2026-01-14 |
| [Veirano Advogados](https://veirano.gupy.io) | Serviços | 2026-01-14 |
| [Vulcabras](https://vulcabras.gupy.io) | Indústria | 2026-01-14 |
| [ConectCar](https://conectcar.gupy.io) | Estratégico | 2026-01-13 |
| [Conta Simples](https://contasimples.gupy.io) | Fintech | 2026-01-13 |
| [Cortex](https://cortex.gupy.io) | 01 - Dados: Analytics & IA | 2026-01-13 |
| [Cyrela](https://cyrela.gupy.io) | Construção | 2026-01-13 |
| [Granado](https://granado.gupy.io) | Cosméticos | 2026-01-13 |
| [Taco](https://taco.gupy.io) | Moda | 2026-01-13 |
| [Webmotors](https://webmotors.gupy.io) | Automotivo | 2026-01-13 |
| [Ambipar](https://ambipar.gupy.io) | Estratégico | 2026-01-12 |
| [Mitre Realty](https://mitrerealty.gupy.io) | Construção | 2026-01-12 |
| [Vibra Energia](https://vibraenergia.gupy.io) | Energia/Petróleo | 2026-01-12 |
| [Alupar](https://alupar.gupy.io) | Estratégico | 2026-01-09 |
| [Grupo SEB](https://gruposeb.gupy.io) | Educação | 2026-01-09 |
| [LOUD](https://loud.gupy.io) | Games | 2026-01-09 |
| [Roldão Atacadista](https://roldao.gupy.io) | Varejo | 2026-01-08 |
| [3coracoes](https://3coracoes.gupy.io) | A Classificar | 2026-01-07 |
| [Ambev Tech](https://ambevtech.gupy.io) | Alimentos e Bebidas | 2026-01-07 |
| [Itaú - Carreiras Internas](https://carreirasinternasitau.gupy.io) | Finanças/Banco & Fintech | 2026-01-07 |
| [Santa Casa BH](https://santacasabh.gupy.io) | Saúde | 2026-01-07 |
| [Aegea](https://aegea.gupy.io) | Saneamento | 2026-01-06 |
| [Banco Sofisa](https://bancosofisa.gupy.io) | Finanças/Banco & Fintech | 2026-01-06 |
| [Coopercitrus](https://coopercitrus.gupy.io) | Alimentos | 2026-01-06 |
| [Fundação Itaú](https://fundacaoitau.gupy.io) | Banco | 2026-01-06 |
| [PagSeguro](https://pagseguro.gupy.io) | Finanças/Banco & Fintech | 2026-01-06 |
| [Riachuelo](https://riachuelo.gupy.io) | Varejo | 2026-01-06 |
| [Gamers Club](https://gamersclub.gupy.io) | Games | 2026-01-05 |
| [Havan](https://havan.gupy.io) | Varejo | 2026-01-05 |
| [Atlantica Hospitality](https://atlantica.gupy.io) | Saúde | 2026-01-02 |
| [Unimed Fortaleza](https://unimedfortaleza.gupy.io) | Saúde | 2026-01-02 |
| [Maria Filó Moda Br](https://mariafilo.gupy.io) | Estratégico | 2025-12-30 |
| [Uello](https://uello.gupy.io) | Estratégico | 2025-12-30 |
| [Fundação Pedro Paes Mendonça](https://fppm.gupy.io) | Social | 2025-12-26 |
| [CLAMED](https://clamed.gupy.io) | Saúde | 2025-12-23 |
| [Nita Alimentos](https://nitaalimentos.gupy.io) | Alimentos e Bebidas | 2025-12-22 |
| [Tahto Atendimento](https://tahto.gupy.io) | Serviços | 2025-12-22 |
| [TranspoTech](https://transpotech.gupy.io) | Logística | 2025-12-18 |
| [Villela Brasil Bank](https://villelabrasilbank.gupy.io) | Finanças | 2025-12-16 |
| [Gafisa](https://gafisa.gupy.io) | Construção | 2025-12-12 |
| [Omie](https://carreirasomie.gupy.io) | SaaS | 2025-12-12 |
| [RTE Rodonaves](https://rodonaves.gupy.io) | Logística | 2025-12-11 |
| [Cogna](https://cogna.gupy.io) | Educação | 2025-12-10 |
| [Ipiranga](https://ipiranga.gupy.io) | Energia/Petróleo | 2025-12-09 |
| [Pottencial Seguradora](https://pottencial.gupy.io) | Finanças/Seguros | 2025-12-09 |
| [Yduqs](https://yduqs.gupy.io) | Educação | 2025-12-08 |
| [Porto](https://porto.gupy.io) | Seguros | 2025-11-28 |
| [Andrade Gutierrez](https://andradegutierrez.gupy.io) | Infraestrutura | 2025-11-27 |
| [Ambev](https://ambev.gupy.io) | Alimentos e Bebidas | 2025-11-26 |
| [GOL Linhas Aéreas](https://golcarreiras.gupy.io) | Aviação | 2025-11-26 |
| [Petz](https://petz.gupy.io) | Pet Shop | 2025-11-26 |
| [BMW Group Brasil](https://bmw.gupy.io) | Automotivo | 2025-11-24 |
| [Coca-Cola Femsa BR](https://cocacolafemsabr.gupy.io) | Alimentos e Bebidas | 2025-11-20 |
| [3tentos](https://3tentos.gupy.io) | Agronegócio | 2025-11-19 |
| [Total Express](https://totalexpress.gupy.io) | Logística | 2025-11-18 |
| [Burger King (Zamp)](https://zamp.gupy.io) | Alimentação | 2025-11-14 |
| [Solar Coca-Cola](https://solarcocacola.gupy.io) | Alimentos e Bebidas | 2025-11-14 |
| [TruckPad](https://truckpad.gupy.io) | Estratégico | 2025-11-12 |
| [SLC Agrícola](https://slcagricola.gupy.io) | Agronegócio | 2025-11-11 |
| [Coplana](https://coplana.gupy.io) | Agronegócio | 2025-11-10 |
| [Unidas](https://unidas.gupy.io) | Aluguel de Veículos | 2025-11-07 |
| [Docket](https://docket.gupy.io) | Tecnologia | 2025-10-29 |
| [Minerva Foods](https://minervafoods.gupy.io) | Alimentos e Bebidas | 2025-10-29 |
| [WEG](https://weg.gupy.io) | Indústria | 2025-10-29 |
| [Wiz Co](https://wiz.gupy.io) | Finanças | 2025-10-15 |
| [EcoRodovias](https://ecorodovias.gupy.io) | Estratégico | 2025-10-13 |
| [Santa Maria Ind](https://santamaria.gupy.io) | Estratégico | 2025-10-06 |
| [Unimed Campinas Oficial](https://unimedcampinas.gupy.io) | Saúde | 2025-10-06 |
| [banQi](https://banqi.gupy.io) | Soluções de Pagamento | 2025-09-30 |
| [ClearSale](https://clearsale.gupy.io) | 01 - Dados: Analytics & IA | 2025-09-25 |
| [Unimed Goiânia Oficial](https://unimedgoiania.gupy.io) | Saúde | 2025-09-23 |
| [Raizen](https://genteraizen.gupy.io) | Energia | 2025-09-19 |
| [Eurofarma](https://eurofarma.gupy.io) | Farmacêutica | 2025-09-17 |
| [Unimed Teresina Oficial](https://unimedteresina.gupy.io) | Saúde | 2025-06-26 |
| [Banco Mercantil](https://mercantil.gupy.io) | Finanças/Banco & Fintech | 2025-05-08 |
| [Grupo Sabin](https://gruposabin.gupy.io) | Saúde | 2025-05-02 |
| [Movida](https://movida.gupy.io) | Automotivo | 2025-04-14 |
| [PUC-SP](https://pucsp.gupy.io) | Educacional | 2025-04-11 |
| [Fluency Academy](https://fluencyacademy.gupy.io) | Educacional | 2025-04-10 |
| [Unimed Porto Alegre](https://unimedpoa.gupy.io) | Saúde | 2025-04-09 |
| [JSL](https://jsl.gupy.io) | Logística | 2025-03-25 |
| [CS Brasil](https://csbrasil.gupy.io) | Logística | 2025-03-17 |
| [Grupo Soma](https://gruposoma.gupy.io) | Varejo | 2025-03-12 |
| [Automob](https://automob.gupy.io) | Automotivo | 2025-02-26 |
| [Le Biscuit Varejo](https://lebiscuit.gupy.io) | Varejo | 2024-09-15 |
| [4mk](https://4mk.gupy.io) | A Classificar | 2024-08-13 |
| [Daycoval DayCambio](https://daycambio.gupy.io) | Banco | 2024-08-09 |
| [Daycoval DayCred](https://daycred.gupy.io) | Banco | 2024-08-09 |
| [Banco Daycoval](https://bancodaycoval.gupy.io) | Finanças/Banco & Fintech | 2024-08-08 |
| [Energisa (Tecnologia)](https://energisatech.gupy.io) | Energia | 2024-07-31 |
| [Yamaha](https://yamaha.gupy.io) | Automotivo | 2024-07-29 |
| [Armac](https://armac.gupy.io) | Estratégico | 2024-02-28 |
| [Usiminas](https://usiminas.gupy.io) | Siderurgia | 2024-01-22 |
| [Aacd](https://aacd.gupy.io) | A Classificar | 2024-01-05 |
| [Red House International School](https://redhouse.gupy.io) | Finanças/Banco & Fintech | 2023-11-16 |
| [Vamos](https://vamos.gupy.io) | Logística | 2023-09-20 |
| [Lojas Ypê](https://carreirasype.gupy.io) | Varejo | 2023-06-22 |
| [Efí Bank](https://sejaefi.gupy.io) | Financeiro | 2023-04-18 |
| [Sami](https://oisami.gupy.io) | Saúde | 2023-01-30 |
| [Aevo](https://aevo.gupy.io) | Tecnologia | 2022-11-18 |
| [Stark Bank](https://stark.gupy.io) | Fintech | 2022-09-20 |
| [Adidas Brasil](https://adidas.gupy.io) | Moda | 2022-07-09 |
| [Faber-Castell](https://fabercastell.gupy.io) | Papelaria | 2022-05-12 |
| [Simpar](https://simpar.gupy.io) | Logística | 2022-01-03 |
| [1Doc](https://1doc.gupy.io) | Saúde |  |
| [3M](https://3m.wd1.myworkdayjobs.com/Search) | Indústria |  |
| [3R Petroleum](https://3rpetroleum.gupy.io) | Energia/Petróleo |  |
| [99 (99Entrega)](https://trabalheconosco.vagas.com.br/99) | Logística/Delivery |  |
| [AB InBev](https://job-boards.greenhouse.io/abinbev) | Alimentos e Bebidas |  |
| [Accenture](https://www.accenture.com/br-pt/careers) | Consultoria |  |
| [Accona](https://www.acciona.com.br/trabalhe-conosco) | Infraestrutura |  |
| [Accor](https://careers.accor.com) | Hospitalidade |  |
| [Acer](https://career10.successfactors.com/career?company=acerincorp) | Eletrônicos |  |
| [Aché Laboratórios](https://trabalheconosco.vagas.com.br/achlaboratrios) | Farmacêutica |  |
| [Activision Blizzard](https://careers.activisionblizzard.com) | Estratégico |  |
| [Adobe](https://adobe.wd5.myworkdayjobs.com/external_experienced) | Tecnologia |  |
| [ADP](https://jobs.adp.com) | Serviços |  |
| [AES Brasil](https://trabalheconosco.vagas.com.br/aesbrasil) | Estratégico |  |
| [Agibank](https://job-boards.greenhouse.io/agibank) | Banco |  |
| [Agilize](https://boards.greenhouse.io/agilize) | Fintech |  |
| [Agoda](https://careersatagoda.com/vacancies/?search&teams&locations) | Tecnologia |  |
| [Agrale](https://trabalheconosco.vagas.com.br/agrale) | Estratégico |  |
| [Ailos Sistema](https://ailos.gupy.io) | Finanças |  |
| [Aiqfome](https://trabalheconosco.vagas.com.br/aiqfome) | Estratégico |  |
| [Air France-KLM](https://recrutement.airfrance.com) | Aviação |  |
| [Airbnb](https://boards.greenhouse.io/airbnb) | Turismo |  |
| [Albert Einstein](https://www.einstein.br/carreiras) | Saúde |  |
| [Albert Einstein](https://trabalheconosco.vagas.com.br/alberteinstein) | A recuperar |  |
| [Alelo](https://alelo.inhire.app/vagas) | Benefícios |  |
| [Algar Telecom](https://trabalheconosco.vagas.com.br/algartelecom) | Telecom |  |
| [Alibaba](https://talent.alibaba.com) | E-commerce |  |
| [Alice](https://alice.inhire.app/vagas) | Healthtech |  |
| [Alliar](https://trabalheconosco.vagas.com.br/alliar) | Estratégico |  |
| [Allied](https://trabalheconosco.vagas.com.br/allied) | Estratégico |  |
| [Allos](https://carreiras.gupy.io/allos) | Shopping |  |
| [Allos](https://trabalheconosco.vagas.com.br/allos) | A recuperar |  |
| [Alteryx](https://www.alteryx.com/careers) | 01 - Dados: Analytics & IA |  |
| [Alura](https://alun.inhire.app/alura/vagas) | Educação |  |
| [Amaggi](https://carreiras.gupy.io/amaggi) | Agronegócio |  |
| [Amaggi](https://trabalheconosco.vagas.com.br/amaggi) | A recuperar |  |
| [Amazon](https://www.amazon.jobs) | Tecnologia |  |
| [Amcham Brasil](https://amcham.gupy.io) | Associação |  |
| [Ame Digital](https://trabalheconosco.vagas.com.br/amedigital) | Estratégico |  |
| [American Airlines](https://jobs.aa.com) | Aviação |  |
| [American Express](https://aexp.eightfold.ai/careers) | Financeiro |  |
| [Amex](https://www.americanexpress.com/en-us/careers) | Financeiro |  |
| [Amil](https://career19.sapsf.com/careers?company=amilassist) | Saúde |  |
| [Analytics](https://analytics.inhire.com.br) | A Classificar |  |
| [Analytics-ss](https://analytics-ss.inhire.com.br) | A Classificar |  |
| [Ânima Educação](https://anima.gupy.io) | Educação |  |
| [Ânima Educação](https://trabalheconosco.vagas.com.br/animaeducacao) | A recuperar |  |
| [Anthropic](https://boards.greenhouse.io/anthropic) | 01 - Dados: Inteligência Artificial |  |
| [Apple](https://www.apple.com/careers/br) | Tecnologia |  |
| [Apptite](https://trabalheconosco.vagas.com.br/apptite) | Estratégico |  |
| [Arco Educação](https://job-boards.greenhouse.io/arcoeducacao) | Educacional |  |
| [Arco Educação](https://boards.greenhouse.io/arcoeducacao) | Educação |  |
| [Arcos Dorados (McDonald s)](https://trabalheconosconamc.infojobs.com.br) | Alimentação |  |
| [Arezzo&Co](https://azzas2154.gupy.io) | Varejo |  |
| [Arteris](https://arteris.gupy.io) | Infraestrutura |  |
| [AstraZeneca](https://astrazeneca.wd3.myworkdayjobs.com/Careers) | Farmacêutica |  |
| [Asus](https://www.asus.com/about-asus/careers) | Tecnologia |  |
| [Atlassian](https://www.atlassian.com/company/careers) | Estratégico |  |
| [AuroraCoop (Aurora Alimentos)](https://trabalheconosco.vagas.com.br/aurora-alimentos) | Alimentos e Bebidas |  |
| [Autodesk](https://www.autodesk.com/careers) | Tecnologia |  |
| [Avanade](https://www.avanade.com/pt-br/career/search-jobs) | Tecnologia |  |
| [Azos](https://azos.inhire.app/vagas) | Fintech |  |
| [Aztec](https://job-boards.eu.greenhouse.io/aztec) | Tecnologia |  |
| [Azul Linhas Aéreas](https://trabalheconosco.vagas.com.br/azullinhasareas) | Logística |  |
| [B3](https://trabalheconosco.vagas.com.br/b3) | Finanças/Banco & Fintech |  |
| [Bacio di Latte](https://trabalheconosco.vagas.com.br/baciodilatte) | Alimentos e Bebidas |  |
| [Bahema Educação](https://trabalheconosco.vagas.com.br/bahemaeducao) | Educação |  |
| [Ball](https://jobs.ball.com/corp_packaging/search) | Embalagens |  |
| [Banco ABC Brasil](https://trabalheconosco.vagas.com.br/bancoabcbrasil) | Finanças/Banco & Fintech |  |
| [Banco BMG](https://bancobmg.gupy.io) | Finanças/Banco & Fintech |  |
| [Banco Bradesco](https://bradesco.csod.com/ux/ats/careersite/1/home?c=bradesco) | Finanças/Banco & Fintech |  |
| [Banco BV](https://jobs.lever.co/bv) | Finanças/Banco & Fintech |  |
| [Banco da Amazônia](https://trabalheconosco.vagas.com.br/bancodaamaznia) | Finanças/Banco & Fintech |  |
| [Banco de Brasília (BRB)](https://trabalheconosco.vagas.com.br/bancodebraslia) | Finanças/Banco & Fintech |  |
| [Banco Digio](https://trabalheconosco.vagas.com.br/bancodigio) | Finanças/Banco & Fintech |  |
| [Banco do Brasil](https://trabalheconosco.vagas.com.br/bancodobrasil) | Finanças/Banco & Fintech |  |
| [Banco do Nordeste](https://trabalheconosco.vagas.com.br/bancodonordeste) | Finanças/Banco & Fintech |  |
| [Banco Inbursa](https://trabalheconosco.vagas.com.br/bancoinbursa) | Finanças/Banco & Fintech |  |
| [Banco Industrial do Brasil](https://trabalheconosco.vagas.com.br/bancoindustrialdobrasil) | Finanças/Banco & Fintech |  |
| [Banco Inter](https://carreiras.gupy.io/bancointer) | Finanças/Banco & Fintech |  |
| [Banco Mercantil do Brasil](https://trabalheconosco.vagas.com.br/bancomercantildobrasil) | Finanças/Banco & Fintech |  |
| [Banco Original](https://original.gupy.io) | Finanças/Banco & Fintech |  |
| [Banco Ourinvest](https://bancoourinvest.gupy.io) | Finanças/Banco & Fintech |  |
| [Banco Pan](https://boards.greenhouse.io/bancopan) | Finanças/Banco & Fintech |  |
| [Banco Paulista](https://trabalheconosco.vagas.com.br/bancopaulista) | Finanças/Banco & Fintech |  |
| [Banco Pine](https://bancopine.inhire.app/vagas) | Finanças/Banco & Fintech |  |
| [Banco Rendimento](https://trabalheconosco.vagas.com.br/bancorendimento) | Finanças/Banco & Fintech |  |
| [Banco Safra](https://trabalheconosco.vagas.com.br/bancosafra) | Finanças/Banco & Fintech |  |
| [Banco Semear](https://trabalheconosco.vagas.com.br/bancosemear) | Finanças/Banco & Fintech |  |
| [Banco Topázio](https://trabalheconosco.vagas.com.br/bancotopzio) | Finanças/Banco & Fintech |  |
| [Banco Votorantim (banco BV)](https://trabalheconosco.vagas.com.br/bancovotorantim) | Finanças/Banco & Fintech |  |
| [Band](https://band.jobs.recrut.ai/#openings) | Comunicação |  |
| [Bandai Namco](https://www.bandainamcoent.com/careers) | Jogos |  |
| [Banestes](https://trabalheconosco.vagas.com.br/banestes) | Finanças/Banco & Fintech |  |
| [Banrisul](https://trabalheconosco.vagas.com.br/banrisul) | Finanças/Banco & Fintech |  |
| [BASF](https://career5.successfactors.eu/career?company=C0000159936P) | Química |  |
| [BASF](https://trabalheconosco.vagas.com.br/basf) | A recuperar |  |
| [Bayer](https://bayer.eightfold.ai/careers) | Farmacêutica |  |
| [BB Seguridade](https://trabalheconosco.vagas.com.br/bbseguridade) | Finanças/Seguros |  |
| [BBC](https://careers.bbc.co.uk) | Mídia |  |
| [Beleaf](https://trabalheconosco.vagas.com.br/beleaf) | Alimentos e Bebidas |  |
| [Belvo](https://belvo.com/careers) | Fintech |  |
| [Beyond 101](https://apply.workable.com/beyond-101) | Tecnologia |  |
| [Biolab](https://trabalheconosco.vagas.com.br/biolab) | Farmacêutica |  |
| [Bitso](https://bitso.com/jobs) | Fintech |  |
| [BizCapital](https://trabalheconosco.vagas.com.br/bizcapital) | Finanças/Banco & Fintech |  |
| [Blackberry](https://www.blackberry.com/us/en/company/careers) | Tecnologia |  |
| [Blau Farmacêutica](https://trabalheconosco.vagas.com.br/blaufarmacutica) | Farmacêutica |  |
| [Blip](https://carreiras.gupy.io/blip) | Tecnologia |  |
| [Blizzard](https://activision.wd1.myworkdayjobs.com/Blizzard_External_Careers) | Entretenimento |  |
| [BNY Mellon](https://bnymellon.eightfold.ai/careers) | Financeiro |  |
| [Bold Snacks](https://trabalheconosco.vagas.com.br/boldsnacks) | Alimentos e Bebidas |  |
| [BoldMetrics](https://boldmetrics.com/careers) | Alimentos e Bebidas |  |
| [Bom pra Crédito](https://trabalheconosco.vagas.com.br/bompracrdito) | Estratégico |  |
| [Booking](https://jobs.booking.com/booking/jobs) | Turismo |  |
| [Booking.com](https://jobs.booking.com) | Turismo |  |
| [Bosch Group](https://careers.smartrecruiters.com/BoschGroup) | Indústria |  |
| [Boulder Colorado](https://bouldercolorado.wd1.myworkdayjobs.com/en-US/External) | Setor Público |  |
| [Box Delivery](https://trabalheconosco.vagas.com.br/boxdelivery) | Logística/Delivery |  |
| [Bradesco](https://banco.bradesco/trabalheconosco) | Bancário |  |
| [Bradesco Seguros](https://bradesco.csod.com/ux/ats/careersite/3/home?c=bradesco) | Finanças/Seguros |  |
| [Braskem](https://epiw.fa.la1.oraclecloud.com/hcmUI/CandidateExperience/pt-BR/sites/CX_1001/requisitions) | Indústria |  |
| [Braspress](https://braspress.pandape.infojobs.com.br) | Logística |  |
| [Brastemp (Whirlpool)](https://carreiras.gupy.io/whirlpool) | Eletrodomesticos |  |
| [Braze](https://job-boards.greenhouse.io/braze) | Tecnologia |  |
| [BRB (Banco de Brasília)](https://trabalheconosco.vagas.com.br/brb) | Finanças/Banco & Fintech |  |
| [BRF](https://trabalheconosco.vagas.com.br/brf) | Alimentos e Bebidas |  |
| [Brinks Brasil](https://trabalheconosco.vagas.com.br/brinksbrasil) | Estratégico |  |
| [BRQ Digital Solutions](https://carreiras.gupy.io/brq) | Tecnologia |  |
| [BTG Pactual](https://boards.greenhouse.io/btgpactual) | Banco |  |
| [Buffer](https://journey.buffer.com) | Tecnologia |  |
| [Burger King](https://carreiras.gupy.io/burgerkingbrasil) | Alimentação |  |
| [ByteDance](https://jobs.bytedance.com/en) | Tecnologia |  |
| [C&A Brasil](https://trabalheconosco.vagas.com.br/cabrasil) | Varejo |  |
| [C6 Bank](https://boards.greenhouse.io/c6bank) | Finanças/Banco & Fintech |  |
| [Cabify](https://job-boards.greenhouse.io/cabify) | Transporte |  |
| [Caesb](https://trabalheconosco.vagas.com.br/caesb) | Saneamento |  |
| [Caffeine Army](https://trabalheconosco.vagas.com.br/caffeinearmy) | Alimentos e Bebidas |  |
| [Cagece](https://trabalheconosco.vagas.com.br/cagece) | Saneamento |  |
| [Caixa Econômica Federal](https://trabalheconosco.vagas.com.br/caixaeconmicafederal) | Finanças/Banco & Fintech |  |
| [Caixa Seguridade](https://trabalheconosco.vagas.com.br/caixaseguridade) | Finanças/Seguros |  |
| [Camargo Corrêa](https://trabalheconosco.vagas.com.br/camargocorra) | Construção |  |
| [Camil](https://trabalheconosco.vagas.com.br/camil) | Alimentos |  |
| [Camil Alimentos](https://platform.senior.com.br/hcmrs/hcm/curriculo/?tenant=camilcombr&tenantdomain=camil.com.br#!/vacancies/list) | Alimentos e Bebidas |  |
| [Canva](https://www.canva.com/careers) | Tecnologia |  |
| [Capco](https://boards.greenhouse.io/capco) | Consultoria |  |
| [Capgemini](https://trabalheconosco.vagas.com.br/capgemini) | Consultoria |  |
| [Cargill](https://careers.cargill.com/en/search-jobs) | Agronegócio |  |
| [CargoX](https://cargox.inhire.app/vagas) | Logística |  |
| [Carrefour Brasil](https://trabalheconosco.vagas.com.br/carrefourbrasil) | Varejo |  |
| [Carreira](https://carreira.inhire.com.br) | A Classificar |  |
| [Casan](https://trabalheconosco.vagas.com.br/casan) | Saneamento |  |
| [CD Projekt Red](https://www.cdprojektred.com/en/jobs) | Jogos |  |
| [Ceg (Naturgy)](https://trabalheconosco.vagas.com.br/ceg) | Estratégico |  |
| [Celcoin](https://celcoin.inhire.app/vagas) | Fintech |  |
| [Celesc](https://trabalheconosco.vagas.com.br/celesc) | Energia |  |
| [Cemig](https://trabalheconosco.vagas.com.br/cemig) | Energia |  |
| [Cheftime](https://trabalheconosco.vagas.com.br/cheftime) | Alimentos e Bebidas |  |
| [CI&T](https://jobs.lever.co/ciandt) | Tecnologia |  |
| [Cielo](https://cielo.inhire.app/vagas) | Soluções de Pagamento |  |
| [Cisco](https://careers.cisco.com/global/en) | Tecnologia |  |
| [Citi](https://careers.citigroup.com) | Bancário |  |
| [Click Entregas](https://trabalheconosco.vagas.com.br/clickentregas) | Logística/Delivery |  |
| [Cloudera](https://www.cloudera.com/careers.html) | Tecnologia |  |
| [CloudWalk](https://jobs.lever.co/cloudwalk) | Fintech |  |
| [Coamo Agroindustrial](https://carreiras.gupy.io/coamo) | Estratégico |  |
| [Cobasi](https://cobasi.pandape.infojobs.com.br) | Varejo |  |
| [Coca-Cola Company](https://coke.wd1.myworkdayjobs.com/coca-cola-careers) | Alimentos e Bebidas |  |
| [Coca-Cola Femsa](https://trabalheconosco.vagas.com.br/femsa) | Alimentos e Bebidas |  |
| [Coca-Cola Femsa Brasil](https://femsa.gupy.io) | Alimentos e Bebidas |  |
| [Colgate-Palmolive](https://jobs.colgate.com) | Bens de Consumo |  |
| [Comercial Zaffari](https://trabalheconosco.vagas.com.br/comercialzaffari) | Varejo |  |
| [Condor Super Center](https://trabalheconosco.vagas.com.br/condorsupercenter) | Varejo |  |
| [Conta Azul](https://trabalheconosco.vagas.com.br/contaazul) | Logística |  |
| [Contabilizei](https://carreiras.gupy.io/contabilizei) | Fintech |  |
| [Coop](https://cooperativadeconsumo.pandape.infojobs.com.br) | Supermercado |  |
| [Cooxupé](https://carreiras.gupy.io/cooxupe) | Agronegócio |  |
| [Copacol](https://trabalheconosco.vagas.com.br/copacol) | Agronegócio |  |
| [Copasa](https://trabalheconosco.vagas.com.br/copasa) | Saneamento |  |
| [Copel](https://trabalheconosco.vagas.com.br/copel) | Energia |  |
| [Cora](https://cora.inhire.app/vagas) | Banco |  |
| [Corel](https://www.corel.com/en/careers) | Tecnologia |  |
| [Coursera](https://about.coursera.org/careers) | Educação |  |
| [CPFL Energia](https://trabalheconosco.vagas.com.br/cpflenergia) | Energia |  |
| [CrowdStrike](https://www.crowdstrike.com/careers) | Cibersegurança |  |
| [CSN](https://trabalheconosco.vagas.com.br/csn) | A recuperar |  |
| [Daki](https://trabalheconosco.vagas.com.br/daki) | Logística/Delivery |  |
| [Danone](https://ptapply-danone.icims.com/jobs/search) | Alimentos e Bebidas |  |
| [Dasa](https://carreiras.gupy.io/dasa) | Saúde |  |
| [Databricks](https://job-boards.greenhouse.io/databricks) | Tecnologia |  |
| [DataDog](https://careers.datadoghq.com/all-jobs) | Tecnologia |  |
| [DataRobot](https://www.datarobot.com/careers) | Tecnologia |  |
| [dbtLabs](https://job-boards.greenhouse.io/dbtlabsinc) | Tecnologia |  |
| [Dell](https://jobs.dell.com/en) | Tecnologia |  |
| [Deloitte](https://app.jobconvo.com/pt-br/careers/Deloitte/ddf2b2f5-cc30-4503-8ec8-458f9869e2ba/#join) | Consultoria |  |
| [Deloitte](https://trabalheconosco.vagas.com.br/deloitte) | A recuperar |  |
| [Delta Air Lines](https://delta.avature.net/en_US/careers) | Aviação |  |
| [Descomplica](https://carreiras.gupy.io/descomplica) | EdTech |  |
| [Desinchá](https://trabalheconosco.vagas.com.br/desinch) | Estratégico |  |
| [Desktop](https://trabalheconosco.vagas.com.br/desktop) | Telecom |  |
| [DiDi (99)](https://careers-didiglobal.icims.com/jobs/search?ss=1&hashed=-625919479) | Logística/Delivery |  |
| [Diferente](https://trabalheconosco.vagas.com.br/diferente) | Estratégico |  |
| [Digibee](https://job-boards.greenhouse.io/digibeeinc) | Tecnologia |  |
| [Direcional](https://trabalheconosco.vagas.com.br/direcional) | Construção |  |
| [dLocal](https://jobs.lever.co/dlocal) | Fintech |  |
| [Dock](https://dock.gupy.io) | Estratégico |  |
| [Docs](https://docs.inhire.com.br) | A Classificar |  |
| [Domino s Pizza](https://dominospizzabrasil.pandape.infojobs.com.br) | Alimentação |  |
| [Domo](https://www.domo.com/company/careers) | Tecnologia |  |
| [Donorbox](https://job-boards.greenhouse.io/donorbox) | Tecnologia |  |
| [DoorDash International](https://boards.greenhouse.io/doordashinternational) | Finanças/Banco & Fintech |  |
| [Dr. Consulta](https://carreiras.gupy.io/drconsulta) | Healthtech |  |
| [Droga Raia / Drogasil (RD Saúde)](https://carreiras.gupy.io/rd) | Estratégico |  |
| [Dropbox](https://dropbox.jobs) | Tecnologia |  |
| [DuckDuckGo](https://jobs.ashbyhq.com/duck-duck-go) | Tecnologia |  |
| [Duolingo](https://careers.duolingo.com) | Educação |  |
| [EA (Electronic Arts)](https://www.ea.com/careers) | Jogos |  |
| [Eaton](https://eaton.eightfold.ai/careers) | Indústria |  |
| [Ebanx](https://boards.greenhouse.io/ebanx) | Finanças/Banco & Fintech |  |
| [Edenred (Ticket)](https://wd3.myworkdaysite.com/pt-BR/recruiting/edenpeople/Edenred_Careers) | Benefícios |  |
| [EDP Brasil](https://jobs.edp.com) | Energia |  |
| [Eightfold](https://pepsico.eightfold.ai/careers) | Tecnologia |  |
| [Electrolux](https://career.electroluxgroup.com) | Eletrodomesticos |  |
| [Electronic Arts](https://jobs.ea.com/en_US/careers) | Entretenimento |  |
| [Eletrobras](https://eletrobras.gupy.io) | Energia |  |
| [Eleva Educação](https://trabalheconosco.vagas.com.br/elevaeducao) | Educação |  |
| [Embaré](https://trabalheconosco.vagas.com.br/embar) | Estratégico |  |
| [Embasa](https://trabalheconosco.vagas.com.br/embasa) | Saneamento |  |
| [Emirates](https://www.emiratesgroupcareers.com) | Aviação |  |
| [EMS](https://ems.izirh.io) | Farmacêutica |  |
| [Eneva](https://trabalheconosco.vagas.com.br/eneva) | Energia/Petróleo |  |
| [Engie Brasil](https://trabalheconosco.vagas.com.br/engiebrasil) | Energia |  |
| [Engie Brasil](https://jobs.engie.com) | Energia |  |
| [Epic Games](https://www.epicgames.com/site/en-US/careers) | Jogos |  |
| [Epson](https://epson.com.br/carreiras) | Tecnologia |  |
| [Ericsson](https://www.ericsson.com/en/careers) | Telecom |  |
| [Ericsson](https://trabalheconosco.vagas.com.br/ericsson) | A recuperar |  |
| [Eternit](https://trabalheconosco.vagas.com.br/eternit) | Indústria |  |
| [Eu Entrego](https://trabalheconosco.vagas.com.br/euentrego) | Logística/Delivery |  |
| [Even](https://trabalheconosco.vagas.com.br/even) | Construção |  |
| [Expedia](https://careers.expediagroup.com) | Estratégico |  |
| [ExxonMobil](https://jobs.exxonmobil.com) | Energia |  |
| [EY](https://www.ey.com/pt_br/careers) | Consultoria |  |
| [Facchini](https://trabalheconosco.vagas.com.br/facchini) | Indústria |  |
| [Fanatee](https://fanatee.com/#careers) | Games |  |
| [Fazenda Futuro (Future Farm)](https://trabalheconosco.vagas.com.br/fazendafuturo) | Alimentos e Bebidas |  |
| [Federação Paulista de Futebol](https://oportunidades.mindsight.com.br/fpf) | Esporte |  |
| [FedEx](https://fedex.wd1.myworkdayjobs.com/FXE-EU_External) | Logística |  |
| [Feedz](https://feedz.inhire.app/vagas) | RH Tech |  |
| [Ferbasa](https://ferbasa.gupy.io) | Estratégico |  |
| [Ferrero](https://www.ferrerocareers.com) | Alimentos |  |
| [FGV - Fundação Getulio Vargas](https://portal.fgv.br/trabalhe-conosco) | Ensino |  |
| [FIAP](https://alura-fiap-pm3.inhire.app/vagas) | Estratégico |  |
| [Figma](https://boards.greenhouse.io/figma) | Tecnologia |  |
| [Flash](https://flash.inhire.app/vagas) | Tecnologia |  |
| [Fleury](https://trabalheconosco.vagas.com.br/grupo-fleury/oportunidades) | Saúde |  |
| [Folha da Manhã](https://trabalheconosco.vagas.com.br/folhadamanh) | Estratégico |  |
| [Food to Save](https://trabalheconosco.vagas.com.br/foodtosave) | Estratégico |  |
| [Ford](https://efds.fa.em5.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/requisitions) | Automotivo |  |
| [Fortinet](https://www.fortinet.com/corporate/careers) | Cibersegurança |  |
| [Four Seasons Hotels](https://fourseasons.wd3.myworkdayjobs.com/Search) | Hospitalidade |  |
| [Fox Corporation](https://www.foxcareers.com) | Mídia |  |
| [Foxbit](https://trabalheconosco.vagas.com.br/foxbit) | Finanças/Banco & Fintech |  |
| [Fras-le](https://trabalheconosco.vagas.com.br/frasle) | Indústria |  |
| [Frete.com](https://trabalheconosco.vagas.com.br/fretecom) | Logística/Delivery |  |
| [Fretebras](https://fretebras.inhire.app/vagas) | Logística |  |
| [Frimesa](https://trabalheconosco.vagas.com.br/frimesa) | Alimentos e Bebidas |  |
| [Frooty](https://trabalheconosco.vagas.com.br/frooty) | Alimentos e Bebidas |  |
| [Fundação Bradesco](https://bradesco.csod.com/ux/ats/careersite/2/home?c=bradesco) | Educacional |  |
| [Garena](https://careers.garena.com/global/careers) | Games |  |
| [Gazin](https://trabalheconosco.vagas.com.br/gazin) | Varejo |  |
| [GE (General Electric)](https://jobs.gecareers.com) | Indústria |  |
| [GE Aerospace](https://careers.geaerospace.com/global/en/search-results) | Tecnologia |  |
| [GE Healthcare](https://careers.gehealthcare.com) | Saúde |  |
| [GE Vernova](https://careers.gevernova.com/global/en/search-results) | Tecnologia |  |
| [General Motors](https://search-careers.gm.com) | Automotivo |  |
| [Gerador](https://gerador.inhire.com.br) | A Classificar |  |
| [Gerdau](https://career19.sapsf.com/careers?company=gerdauacos) | Indústria |  |
| [Geru](https://trabalheconosco.vagas.com.br/geru) | Finanças/Banco & Fintech |  |
| [GFT Tecnologia](https://career5.successfactors.eu/careers?company=gfttechnol) | Estratégico |  |
| [Gigster](https://virtasant.teamtailor.com) | Tecnologia |  |
| [Giross](https://trabalheconosco.vagas.com.br/giross) | Logística/Delivery |  |
| [GitHub](https://github.com/about/careers) | Tecnologia |  |
| [GitHub Inc](https://globalcareers-githubinc.icims.com/jobs) | Tecnologia |  |
| [GM Financial](https://careers.gmfinancial.com/jobs) | Estratégico |  |
| [Google](https://www.google.com/about/careers/applications/jobs/results) | Tecnologia |  |
| [GoPro](https://gopro.com/en/us/careers) | Tecnologia |  |
| [Gorila](https://carreiras.gupy.io/gorila) | Fintech |  |
| [Grammarly](https://www.grammarly.com/jobs) | Tecnologia |  |
| [Granero](https://trabalheconosco.vagas.com.br/granero) | Estratégico |  |
| [Greenhouse](https://job-boards.greenhouse.io/greenhouse) | Tecnologia |  |
| [Grendene](https://trabalheconosco.vagas.com.br/grendene) | Indústria |  |
| [Gringo](https://gringo.inhire.app/vagas) | Serviços |  |
| [Grupo Águia Branca](https://trabalheconosco.vagas.com.br/grupoguiabranca) | Estratégico |  |
| [Grupo Carrefour](https://corporativo-grupocarrefourbrasil.pandape.infojobs.com.br) | Varejo |  |
| [Grupo Casas Bahia](https://carreiras.gupy.io/grupocasasbahia) | Estratégico |  |
| [Grupo Despegar (Decolar.com)](https://jobs.lever.co/despegar) | Viagens |  |
| [Grupo Fleury](https://trabalheconosco.vagas.com.br/grupo-fleury) | Saúde |  |
| [Grupo Gontijo](https://trabalheconosco.vagas.com.br/grupogontijo) | Estratégico |  |
| [Grupo Habib's](https://grupohabibs.pandape.infojobs.com.br) | Alimentação |  |
| [Grupo Mateus](https://trabalheconosco.vagas.com.br/grupomateus) | Estratégico |  |
| [Grupo Muffato](https://trabalheconosco.vagas.com.br/grupomuffato) | Estratégico |  |
| [Grupo NC](https://trabalheconosco.vagas.com.br/gruponc) | Estratégico |  |
| [Grupo Primo](https://jobs.quickin.io/grupo-primo/jobs) | Consultoria |  |
| [Grupo RV](https://gruporv.pandape.infojobs.com.br) | Varejo |  |
| [Grupo Silvio Santos](https://trabalheconosco.vagas.com.br/gruposilviosantos) | Estratégico |  |
| [Gupy Tecnologia](https://gupy.gupy.io) | Estratégico |  |
| [Habib s](https://carreiras.gupy.io/habibs) | Alimentação |  |
| [Hapvida NotreDame Intermédica](https://hapvidandi.pandape.infojobs.com.br) | Saúde |  |
| [Hashdex](https://trabalheconosco.vagas.com.br/hashdex) | Estratégico |  |
| [HBO (Warner Bros. Discovery)](https://careers.wbd.com/global/en) | Mídia |  |
| [HDI Seguros](https://hdiseguros.gupy.io) | Finanças/Seguros |  |
| [Heineken](https://careers.theheinekencompany.com/Brazil/search) | Alimentos e Bebidas |  |
| [Hidrovias do Brasil](https://trabalheconosco.vagas.com.br/hidroviasdobrasil) | Estratégico |  |
| [Hilton](https://jobs.hilton.com) | Hospitalidade |  |
| [Hinode](https://trabalheconosco.vagas.com.br/hinode) | Estratégico |  |
| [Hootsuite](https://careers.hootsuite.com) | Tecnologia |  |
| [Hopper](https://www.hopper.com/careers) | Turismo |  |
| [Hospital IGESP](https://www.vagas.com.br/vagas-de-igesp) | Saúde |  |
| [Hospital Sírio-Libanês](https://career19.sapsf.com/careers?company=sociedad02) | Saúde |  |
| [Hotmart](https://boards.eu.greenhouse.io/hotmartcareersbr) | Tecnologia |  |
| [HubSpot](https://www.hubspot.com/careers) | Tecnologia |  |
| [Hyatt](https://careers.hyatt.com) | Hospitalidade |  |
| [Hyland](https://careers-hyland.icims.com/jobs/search?ss=1&hashed=-435679902) | Tecnologia |  |
| [IBM](https://www.ibm.com/br-pt/careers) | Tecnologia |  |
| [Icatu Seguros](https://trabalheconosco.vagas.com.br/icatuseguros) | Finanças/Seguros |  |
| [ICIMS](https://careers.icims.com/careers-home/jobs) | Tecnologia |  |
| [iFood](https://job-boards.greenhouse.io/ifoodcarreiras) | Logística/Delivery |  |
| [Iguatemi](https://trabalheconosco.vagas.com.br/iguatemi) | Estratégico |  |
| [Ilegra](https://vagas.ilegra.com) | Tecnologia |  |
| [ília](https://boards.greenhouse.io/ilia) | Estratégico |  |
| [Infracommerce](https://trabalheconosco.vagas.com.br/infracommerce) | Estratégico |  |
| [Inkrypton](https://inkrypton.inhire.com.br) | A Classificar |  |
| [Intel](https://jobs.intel.com) | Tecnologia |  |
| [Inter](https://boards.greenhouse.io/inter) | Finanças/Banco & Fintech |  |
| [Intera](https://vagasbyintera.inhire.app/vagas) | Finanças/Banco & Fintech |  |
| [Involves](https://involves.inhire.app/vagas) | Trade Marketing |  |
| [IQVIA](https://jobs.iqvia.com/en/search-jobs) | Estratégico |  |
| [Irani Papel e Embalagem](https://trabalheconosco.vagas.com.br/iranipapeleembalagem) | Estratégico |  |
| [Isa CTEEP](https://trabalheconosco.vagas.com.br/isacteep) | Estratégico |  |
| [Isaac](https://boards.greenhouse.io/isaac) | Financeiro |  |
| [Itambé](https://trabalheconosco.vagas.com.br/itamb) | Estratégico |  |
| [Itapemirim (Nova Itapemirim)](https://trabalheconosco.vagas.com.br/itapemirim) | Estratégico |  |
| [Itaú Unibanco](https://trabalheconosco.vagas.com.br/itaunibanco) | Finanças/Banco & Fintech |  |
| [ITV](https://www.itvjobs.com) | Mídia |  |
| [Iugu](https://iugu.inhire.app/vagas) | Fintech |  |
| [JD.com](https://corporate.jd.com/careers) | E-commerce |  |
| [João Fortes](https://trabalheconosco.vagas.com.br/joofortes) | Estratégico |  |
| [John Deere](https://johndeere.eightfold.ai/careers) | Indústria |  |
| [Johnson & Johnson](https://www.careers.jnj.com) | Saúde |  |
| [JPMorgan Chase](https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/requisitions) | Financeiro |  |
| [Jungle](https://trabalheconosco.vagas.com.br/jungle) | Estratégico |  |
| [JusBrasil](https://boards.greenhouse.io/jusbrasil) | Tecnologia |  |
| [Kalunga](https://trabalheconosco.vagas.com.br/kalunga) | Estratégico |  |
| [Kanastra](https://kanastra.inhire.app/vagas) | Fintech |  |
| [Kangu](https://trabalheconosco.vagas.com.br/kangu) | Estratégico |  |
| [Kaspersky](https://careers.kaspersky.com) | Cibersegurança |  |
| [Kavak](https://kavakcom.pandape.infojobs.com.br) | Automotivo |  |
| [Kepler Weber](https://trabalheconosco.vagas.com.br/keplerweber) | Estratégico |  |
| [Keyrus](https://jobs.keyrus.com.br/jobs) | Consultoria |  |
| [Khan Academy](https://www.khanacademy.org/about/careers) | Educação |  |
| [Kimberly-Clark](https://kimberlyclark.wd1.myworkdayjobs.com/GLOBAL) | Produtos de Consumo |  |
| [Kiwify](https://kiwify.inhire.app/vagas) | Tecnologia |  |
| [Klabin](https://klabin.inhire.app/vagas) | Indústria |  |
| [Kora Saúde](https://trabalheconosco.vagas.com.br/korasade) | Saúde |  |
| [KPMG](https://kpmg.com/br/pt/home/carreiras.html) | Consultoria |  |
| [KPMG Brasil](https://carreira.inhire.com.br/carreiras/kpmg) | Consultoria |  |
| [Kraft Heinz](https://careers.kraftheinz.com/job-search-results) | Alimentos e Bebidas |  |
| [Kwan](https://kwan.com/careers/#jobpost) | Tecnologia |  |
| [Lalamove Brasil](https://trabalheconosco.vagas.com.br/lalamovebrasil) | Estratégico |  |
| [Lar Cooperativa](https://trabalheconosco.vagas.com.br/lar) | Agronegócio |  |
| [Launchpad Technologies](https://job-boards.greenhouse.io/launchpadtechnologiesinc) | TI |  |
| [Lavvi](https://trabalheconosco.vagas.com.br/lavvi) | Estratégico |  |
| [LEGO](https://lego.wd103.myworkdayjobs.com/LEGO_External) | Tecnologia |  |
| [Lenovo](https://jobs.lenovo.com) | Tecnologia |  |
| [Leroy Merlin](https://carreiras.leroymerlin.com.br) | Varejo |  |
| [Letrus](https://letrus.inhire.app/vagas) | Tecnologia |  |
| [LevelUp](https://trampos.co/level-up) | Games |  |
| [Levo](https://trabalheconosco.vagas.com.br/levo) | Estratégico |  |
| [LG](https://www.lg.com/global/careers) | Tecnologia |  |
| [Libbs](https://trabalheconosco.vagas.com.br/libbs) | Estratégico |  |
| [Liberty Seguros](https://libertyseguros.gupy.io) | Finanças/Seguros |  |
| [Librelato](https://trabalheconosco.vagas.com.br/librelato) | Estratégico |  |
| [Light](https://trabalheconosco.vagas.com.br/light) | Energia |  |
| [LinkedIn](https://careers.linkedin.com) | Tecnologia |  |
| [LinkedIn Brasil](https://linkedin.gupy.io) | Redes Sociais |  |
| [Linx](https://carreiras.gupy.io/linx) | Tecnologia |  |
| [Linx](https://boards.greenhouse.io/linx) | Varejo Tech |  |
| [Liv Up](https://trabalheconosco.vagas.com.br/livup) | Estratégico |  |
| [Live Nation](https://www.livenationentertainment.com/careers) | Entretenimento |  |
| [Local Frio](https://trabalheconosco.vagas.com.br/localfrio) | Estratégico |  |
| [Locaweb](https://locaweb.gupy.io) | Tecnologia |  |
| [Loews Hotels](https://www.loewshotels.com/careers) | Hospitalidade |  |
| [Loft](https://loft.teamtailor.com/jobs) | Tecnologia |  |
| [Log Commercial Properties](https://trabalheconosco.vagas.com.br/logcommercialproperties) | Estratégico |  |
| [Loggi](https://apply.workable.com/loggi) | Logística/Delivery |  |
| [Loggi Tecnologia](https://loggi.gupy.io) | Logística/Delivery |  |
| [Login Logística](https://trabalheconosco.vagas.com.br/loginlogstica) | Logística |  |
| [Logitech](https://www.logitech.com/careers) | Tecnologia |  |
| [Lojas Cem](https://trabalheconosco.vagas.com.br/lojascem) | Varejo |  |
| [Lojas Quero-Quero](https://trabalheconosco.vagas.com.br/lojasqueroquero) | Varejo |  |
| [Lufthansa](https://www.lufthansagroup.careers) | Aviação |  |
| [Mackenzie](https://mackenzie.br/trabalhe-conosco) | Educação |  |
| [MadeiraMadeira](https://carreiras.gupy.io/madeiramadeira) | E-commerce |  |
| [Madero](https://carreiras.gupy.io/madero) | Alimentação |  |
| [Magalu](https://magazineluiza.inhire.app) | Varejo |  |
| [Magazine Luiza](https://trabalheconosco.vagas.com.br/magazineluiza) | Varejo |  |
| [Magnetis](https://trabalheconosco.vagas.com.br/magnetis) | Estratégico |  |
| [Mais Mu](https://trabalheconosco.vagas.com.br/maismu) | Estratégico |  |
| [Mapfre Brasil](https://trabalheconosco.vagas.com.br/mapfrebrasil) | Estratégico |  |
| [Marcopolo](https://trabalheconosco.vagas.com.br/marcopolo) | Indústria |  |
| [Marfrig](https://trabalheconosco.vagas.com.br/marfrig) | Alimentos e Bebidas |  |
| [Marisa](https://carreiras.gupy.io/marisa) | Varejo |  |
| [Marriott International](https://jobs.marriott.com) | Finanças/Banco & Fintech |  |
| [Mart Minas](https://trabalheconosco.vagas.com.br/martminas) | Estratégico |  |
| [Martins Atacado Var](https://martins.gupy.io) | Varejo |  |
| [Mash](https://mash.pandape.infojobs.com.br) | Comércio |  |
| [Mastercard](https://mastercard.wd1.myworkdayjobs.com/CorporateCareers) | Financeiro |  |
| [MasterClass](https://boards.greenhouse.io/masterclass) | Entretenimento |  |
| [Mater Dei](https://trabalheconosco.vagas.com.br/materdei) | Estratégico |  |
| [Meituan](https://zhaopin.meituan.com/en) | Tecnologia |  |
| [Melhor Envio](https://melhorenvio.gupy.io) | Estratégico |  |
| [Melhoramentos](https://trabalheconosco.vagas.com.br/melhoramentos) | Estratégico |  |
| [Meliuz](https://meliuz.inhire.app/vagas) | Fintech |  |
| [Méliuz](https://trabalheconosco.vagas.com.br/mliuz) | Estratégico |  |
| [Melnick](https://trabalheconosco.vagas.com.br/melnick) | Estratégico |  |
| [Mercado Bitcoin](https://mercadobitcoin.inhire.app/vagas) | Fintech |  |
| [Mercado Livre](https://mercadolibre.eightfold.ai/careers) | E-commerce |  |
| [Mercantil do Brasil](https://trabalheconosco.vagas.com.br/mercantildobrasil) | Estratégico |  |
| [Mercedes-Benz Brasil](https://mercedes-benz.gupy.io) | Automotivo |  |
| [Metha (antiga OAS)](https://trabalheconosco.vagas.com.br/metha) | Estratégico |  |
| [Michelin](https://michelinhr.wd3.myworkdayjobs.com/Michelin) | Indústria |  |
| [Microsoft](https://careers.microsoft.com) | Tecnologia |  |
| [Mimic](https://trabalheconosco.vagas.com.br/mimic) | Estratégico |  |
| [Mindbody](https://co.mindbodyonline.com/careers/opportunities) | Tecnologia |  |
| [Mineirao Atacarejo](https://mineirao.gupy.io) | Varejo |  |
| [MJV](https://mjv.inhire.app/vagas) | Consultoria |  |
| [Mobly](https://trabalheconosco.vagas.com.br/mobly) | Varejo |  |
| [Mombora](https://trabalheconosco.vagas.com.br/mombora) | Estratégico |  |
| [Mondelez Internacional](https://wd3.myworkdaysite.com/en-US/recruiting/mdlz/External) | Finanças/Banco & Fintech |  |
| [Mondial Eletrodomésticos](https://selecaogrupomk.vagas.solides.com.br) | Estratégico |  |
| [Motorola Solutions](https://motorolasolutions.wd5.myworkdayjobs.com/Careers) | Tecnologia |  |
| [Mottu](https://trabalheconosco.vagas.com.br/mottu) | Estratégico |  |
| [Moura Dubeux](https://trabalheconosco.vagas.com.br/mouradubeux) | Construção |  |
| [MRS Logística](https://trabalheconosco.vagas.com.br/mrslogstica) | Logística |  |
| [MRV](https://www.mrv.com.br/trabalhe-conosco) | Construção |  |
| [Multiplan](https://trabalheconosco.vagas.com.br/multiplan) | Estratégico |  |
| [Nadara](https://nadara.wd3.myworkdayjobs.com/External) | Tecnologia |  |
| [Natura&CO (Avon + The Body Shop)](https://avon.wd5.myworkdayjobs.com/NaturaCarreiras) | Cosméticos |  |
| [NBCUniversal](https://www.nbcunicareers.com) | Mídia |  |
| [Neoenergia](https://carreiras.gupy.io/neoenergia) | Energia |  |
| [Neogrid](https://trabalheconosco.vagas.com.br/neogrid) | Estratégico |  |
| [Neon](https://jobs.lever.co/neon) | Banco |  |
| [Nestlé](https://jobdetails.nestle.com) | Alimentos e Bebidas |  |
| [Netbr](https://careers.smartrecruiters.com/Netbr) | Tecnologia |  |
| [Netflix](https://jobs.netflix.com) | Mídia |  |
| [Neurotech](https://neurotech.jobs.recrut.ai/#openings) | Tecnologia |  |
| [New](https://new.inhire.com.br) | A Classificar |  |
| [Nissan](https://www.nissan.com.br/trabalhe-conosco.html) | Automotivo |  |
| [Nomad](https://carreiras.gupy.io/nomad) | Fintech |  |
| [Nomad Global](https://apply.workable.com/nomadglobal) | Tecnologia |  |
| [Notion](https://jobs.ashbyhq.com/notion) | Tecnologia |  |
| [NovaDAX](https://trabalheconosco.vagas.com.br/novadax) | Estratégico |  |
| [Novo](https://novo.inhire.com.br) | A Classificar |  |
| [Novonor (Odebrecht)](https://trabalheconosco.vagas.com.br/novonor) | Estratégico |  |
| [NTT Data](https://careers.emeal.nttdata.com/s/jobs?language=pt_BR) | Tecnologia |  |
| [Nubank](https://boards.greenhouse.io/nubank) | Finanças/Banco & Fintech |  |
| [Nubank (Nu Holdings)](https://trabalheconosco.vagas.com.br/nubank) | Finanças/Banco & Fintech |  |
| [Nude.](https://trabalheconosco.vagas.com.br/nude) | Estratégico |  |
| [O Estado de S. Paulo](https://trabalheconosco.vagas.com.br/oestadodespaulo) | Estratégico |  |
| [Oakberry](https://trabalheconosco.vagas.com.br/oakberry) | Estratégico |  |
| [OdontoPrev](https://odontoprev.gupy.io) | Saúde |  |
| [Odous de Deus](https://odous dedeus.gupy.io) | Farmacêutica |  |
| [OEC](https://trabalheconosco.vagas.com.br/oec) | Construção |  |
| [OEC (Odebrecht)](https://oec-eng.com/trabalhe-conosco) | Infraestrutura |  |
| [Olga Ri](https://trabalheconosco.vagas.com.br/olgari) | Estratégico |  |
| [Olist](https://olist.inhire.app/vagas) | Tecnologia |  |
| [Oncoclínicas](https://trabalheconosco.vagas.com.br/oncoclnicas) | Estratégico |  |
| [ONR – Registro de Imóveis Eletrônico](https://jobs.quickin.io/registradores/jobs) | Registro de Imóveis Eletrônico |  |
| [Open Co](https://carreiras.gupy.io/openco) | Fintech |  |
| [Oracle](https://www.oracle.com/careers) | Tecnologia |  |
| [Órama Investimentos](https://trabalheconosco.vagas.com.br/ramainvestimentos) | Telecom |  |
| [Outback (Bloomin Brands)](https://carreiras.gupy.io/bloominbrands) | Alimentação |  |
| [OXXO](https://oxxo.eightfold.ai/careers) | Varejo |  |
| [OYO Rooms](https://www.oyorooms.com/careers) | Hospitalidade |  |
| [P&G](https://www.pgcareers.com/br/en) | Bens de Consumo |  |
| [Pacaembu Construtora](https://pacaembu.gupy.io) | Construção |  |
| [Pagar.me](https://pagarme.gupy.io) | Fintech |  |
| [PagBank](https://carreiras.gupy.io/pagbank) | Finanças/Banco & Fintech |  |
| [PagBank (PagSeguro)](https://trabalheconosco.vagas.com.br/pagbank) | Finanças/Banco & Fintech |  |
| [Pague Menos](https://trabalheconosco.vagas.com.br/paguemenos) | Estratégico |  |
| [Panvel (Dimed)](https://panvel.gupy.io) | Estratégico |  |
| [Paramount](https://careers.paramount.com) | Mídia |  |
| [Paraná Banco](https://jobs.quickin.io/paranabanco/jobs) | Finanças/Banco & Fintech |  |
| [Passbolt](https://passbolt.inhire.com.br) | A Classificar |  |
| [Payclip](https://payclip.bamboohr.com/careers) | Fintech |  |
| [Paypal](https://paypal.eightfold.ai/careers) | Financeiro |  |
| [PepsiCo](https://www.pepsicojobs.com/main) | Alimentos |  |
| [Pernambucanas](https://vemprafamilia-pernambucanas.cliqx.com.br) | Varejo |  |
| [Petlove](https://petlove.jobs.recrut.ai) | Pet |  |
| [Petrobras](https://petrobras.com.br/pt/quem-somos/carreiras) | Energia/Petróleo |  |
| [Pfizer](https://pfizer.wd1.myworkdayjobs.com/PfizerCareers) | Farmacêutica |  |
| [PicPay](https://boards.greenhouse.io/picpay) | Fintech |  |
| [Pipefy](https://app.pipefy.com/organizations/28/interfaces/445e5dd7-d23f-4299-8777-9280272d015d/pages/83bf9609-eb1c-4f7c-8103-c6cc2170aeb0) | Software |  |
| [Pismo](https://trabalheconosco.vagas.com.br/pismo) | Estratégico |  |
| [Plano & Plano](https://trabalheconosco.vagas.com.br/planoplano) | Estratégico |  |
| [PlayDelivery](https://trabalheconosco.vagas.com.br/playdelivery) | Estratégico |  |
| [Pleo](https://boards.greenhouse.io/pleo) | Fintech |  |
| [Polishop](https://trabalheconosco.vagas.com.br/polishop) | Varejo |  |
| [Positive Brands](https://trabalheconosco.vagas.com.br/positivebrands) | Estratégico |  |
| [Pravaler](https://trabalheconosco.vagas.com.br/pravaler) | Indústria |  |
| [Prevent Senior](https://www.preventsenior.com.br/trabalhe-conosco) | Saúde |  |
| [Prosegur Brasil](https://trabalheconosco.vagas.com.br/prosegurbrasil) | Estratégico |  |
| [Protege](https://trabalheconosco.vagas.com.br/protege) | Estratégico |  |
| [Proton](https://job-boards.eu.greenhouse.io/proton) | Tecnologia |  |
| [PwC Global](https://pwc.wd3.myworkdayjobs.com/Global_Experienced_Careers) | Consultoria |  |
| [PwC Portugal](https://pwcportugal.csod.com/ux/ats/careersite/4/home?c=pwcportugal) | Consultoria |  |
| [Qatar Airways](https://careers.qatarairways.com/global/en) | Aviação |  |
| [QI Tech](https://qitech.inhire.app) | Fintech |  |
| [Qlik](https://www.qlik.com/us/company/careers) | Tecnologia |  |
| [Qualicorp](https://trabalheconosco.vagas.com.br/qualicorp) | Estratégico |  |
| [Queiroz Galvão](https://trabalheconosco.vagas.com.br/queirozgalvo) | Estratégico |  |
| [Quinto Andar](https://job-boards.greenhouse.io/quintoandar) | Imóveis |  |
| [QuintoAndar](https://boards.greenhouse.io/quintoandar) | Proptech |  |
| [Rabobank](https://www.rabobank.com/careers) | Financeiro |  |
| [Raízs](https://trabalheconosco.vagas.com.br/razs) | Estratégico |  |
| [Rapiddo](https://trabalheconosco.vagas.com.br/rapiddo) | Estratégico |  |
| [Rappi](https://rappi.wd12.myworkdayjobs.com/es/Rappi_jobs) | Logística/Delivery |  |
| [Razer](https://razer.wd3.myworkdayjobs.com/Careers) | Games |  |
| [RBS](https://trabalheconosco.vagas.com.br/rbs) | Estratégico |  |
| [RD Station](https://boards.greenhouse.io/rdstation) | Tecnologia |  |
| [Real Expresso](https://realexpresso.gupy.io) | Estratégico |  |
| [Rebel](https://trabalheconosco.vagas.com.br/rebel) | Estratégico |  |
| [RecargaPay](https://apply.workable.com/recargapay) | Tecnologia |  |
| [Red Bull](https://jobs.redbull.com/br-pt) | Alimentos e Bebidas |  |
| [Rede D Or](https://trabalheconosco.vagas.com.br/rede-dor-sao-luiz) | Saúde |  |
| [Rede Dor](https://trabalheconosco.vagas.com.br/rededor) | Saúde |  |
| [Rede DOr São Luiz](https://www.vagas.com.br/vagas-de-rededor) | Saúde |  |
| [Remotecom](https://job-boards.greenhouse.io/remotecom) | Tecnologia |  |
| [Riot Games](https://www.riotgames.com/pt-br/trabalhe-conosco#job-list) | Games |  |
| [Rippling](https://ats.rippling.com/careers-quartile/jobs) | Tecnologia |  |
| [Roche](https://roche.wd3.myworkdayjobs.com/roche-ext) | Farmacêutica |  |
| [Rockstar Games](https://www.rockstargames.com/careers/openings) | Games |  |
| [Romi](https://trabalheconosco.vagas.com.br/romi) | Estratégico |  |
| [Rossi Residencial](https://trabalheconosco.vagas.com.br/rossiresidencial) | Estratégico |  |
| [Rumo](https://trabalheconosco.vagas.com.br/rumo) | Logística |  |
| [Ryanair](https://careers.ryanair.com/jobs) | Aviação |  |
| [Sabesp](https://carreiras.gupy.io/sabesp) | Saneamento |  |
| [Salesforce](https://www.salesforce.com/company/careers) | Tecnologia |  |
| [Samsung](https://sec.wd3.myworkdayjobs.com/Samsung_Careers) | Eletrônicos |  |
| [Saneago](https://trabalheconosco.vagas.com.br/saneago) | Saneamento |  |
| [Sanepar](https://trabalheconosco.vagas.com.br/sanepar) | Saneamento |  |
| [Sanofi](https://sanofi.wd3.myworkdayjobs.com/SanofiCareers) | Farmacêutica |  |
| [Santander](https://www.santander.com.br/hotsite/carreiras) | Bancário |  |
| [Santander Brasil](https://trabalheconosco.vagas.com.br/santanderbrasil) | Estratégico |  |
| [Santos Brasil](https://trabalheconosco.vagas.com.br/santosbrasil) | Estratégico |  |
| [São Martinho](https://trabalheconosco.vagas.com.br/somartinho) | Estratégico |  |
| [SAP](https://jobs.sap.com) | Tecnologia |  |
| [Savegnago](https://trabalheconosco.vagas.com.br/savegnago) | Estratégico |  |
| [SBT](https://carreiras.gupy.io/sbt) | Mídia |  |
| [Schulz](https://trabalheconosco.vagas.com.br/schulz) | Estratégico |  |
| [Sebrae](https://sebrae.com.br) | Serviços |  |
| [Semantix](https://jobs.quickin.io/semantix/jobs) | Tecnologia |  |
| [Senac](https://www.senac.br) | Educação |  |
| [Senior Sistemas](https://carreiras.gupy.io/senior) | Tecnologia |  |
| [Sensor Tower](https://jobs.lever.co/sensortower) | Tecnologia |  |
| [Ser Educacional](https://trabalheconosco.vagas.com.br/sereducacional) | Educação |  |
| [Serasa Experian](https://careers.smartrecruiters.com/experian) | 01 - Dados: Analytics & IA |  |
| [Shape Digital](https://shapedigital.inhire.app/vagas) | Tecnologia |  |
| [Shell](https://carreiras.gupy.io/shell) | Energia |  |
| [Shipp](https://trabalheconosco.vagas.com.br/shipp) | Estratégico |  |
| [Shopee](https://careers.shopee.com.br/jobs) | Comércio Eletrônico |  |
| [Siemens](https://carreiras.gupy.io/siemens) | Indústria |  |
| [Siemens Healthineers](https://carreiras.gupy.io/siemens-healthineers) | Saúde |  |
| [Sinch](https://apply.workable.com/sinch) | Tecnologia |  |
| [Singapore Airlines](https://www.singaporeair.com/en_UK/sg/careers) | Aviação |  |
| [Sirio-Libanes](https://www.hospitalsiriolibanes.org.br/trabalhe-conosco) | Saúde |  |
| [Smart Fit](https://trabalheconosco.vagas.com.br/smartfit) | Estratégico |  |
| [Smart Kitchens](https://trabalheconosco.vagas.com.br/smartkitchens) | Estratégico |  |
| [Sode](https://trabalheconosco.vagas.com.br/sode) | Estratégico |  |
| [Sodexo](https://sodexobeneficios.gupy.io) | Serviços |  |
| [Sodexo (Pluxee Brasil)](https://trabalheconosco.vagas.com.br/sodexo) | Estratégico |  |
| [Sólides](https://vagas.solides.com.br) | HR Tech |  |
| [SONDA](https://career8.successfactors.com/career?company=SONDAP) | Tecnologia |  |
| [Sony Global](https://sonyglobal.wd1.myworkdayjobs.com/en-US/SonyGlobalCareers) | Entretenimento |  |
| [Sony Interactive Entertainment Global](https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal) | Finanças/Banco & Fintech |  |
| [Sony Music](https://boards.greenhouse.io/sonymusicentertainment) | Entretenimento |  |
| [Sopra Steria](https://careers.soprasteria.co.uk/uk/en/job-search) | Estratégico |  |
| [Sourcegraph](https://boards.greenhouse.io/sourcegraph91) | Tecnologia |  |
| [SPDM Hospital São Paulo](https://spdm.gupy.io) | Saúde |  |
| [Speedbird Aero](https://trabalheconosco.vagas.com.br/speedbirdaero) | Estratégico |  |
| [Spotify](https://www.lifeatspotify.com) | Mídia |  |
| [Stellantis](https://careers.stellantis.com) | Automotivo |  |
| [Stone](https://job-boards.greenhouse.io/stone) | Finanças/Banco & Fintech |  |
| [Stone](https://boards.greenhouse.io/stone) | Finanças/Banco & Fintech |  |
| [Stone](https://stone.gupy.io) | Finanças/Banco & Fintech |  |
| [Super Nosso](https://supernosso.recrut.ai) | Varejo |  |
| [Superdigital](https://trabalheconosco.vagas.com.br/superdigital) | Estratégico |  |
| [Supermercados BH](https://trabalheconosco.vagas.com.br/supermercadosbh) | Varejo |  |
| [Supportiv](https://supportiv.bamboohr.com/careers) | Saúde |  |
| [Suzano](https://suzano.inhire.app/vagas) | Indústria |  |
| [Swap](https://trabalheconosco.vagas.com.br/swap) | Estratégico |  |
| [Swile](https://jobs.lever.co/swile) | Tecnologia |  |
| [Swile Brasil](https://trabalheconosco.vagas.com.br/swilebrasil) | Estratégico |  |
| [Sympla](https://sympla.inhire.app/vagas) | Tecnologia |  |
| [T-Systems Brasil](https://www.t-systems.com/br/pt/carreiras) | Tecnologia |  |
| [T4F - Time for Fun](https://t4f.vagas.solides.com.br) | Telecom |  |
| [Taesa](https://trabalheconosco.vagas.com.br/taesa) | Estratégico |  |
| [TakeBlip](https://job-boards.greenhouse.io/blip-global) | Tecnologia |  |
| [Team Liquid](https://careers.teamliquid.com/#jobs) | Games |  |
| [Telefônica Brasil (Vivo)](https://trabalheconosco.vagas.com.br/telefnicabrasil) | Telecom |  |
| [Telhanorte](https://www.vagas.com.br/vagas-de-telhanorte) | Varejo |  |
| [Telus Digital BR](https://telusdigital.com/careers) | Tecnologia |  |
| [Tembici](https://carreiras.gupy.io/tembici) | Mobilidade |  |
| [Terra Santa](https://trabalheconosco.vagas.com.br/terrasanta) | Estratégico |  |
| [The New](https://trabalheconosco.vagas.com.br/thenew) | Estratégico |  |
| [ThoughtWorks](https://www.thoughtworks.com/careers/jobs) | Tecnologia |  |
| [Ticket (Edenred Brasil)](https://trabalheconosco.vagas.com.br/ticket) | Estratégico |  |
| [TIM Brasil](https://trabalheconosco.vagas.com.br/timbrasil) | Telecom |  |
| [TIVIT](https://talent.gupy.io/tivit) | Tecnologia |  |
| [Tok&Stok](https://tokstok.pandape.infojobs.com.br) | Varejo |  |
| [Totvs](https://carreiras.gupy.io/totvs) | Tecnologia |  |
| [Toyota](https://carreiras.gupy.io/toyota) | Automotivo |  |
| [Toyota Brasil](https://toyota.wd503.myworkdayjobs.com/pt-BR/TLAC) | Automotivo |  |
| [Track&Field](https://trabalheconosco.vagas.com.br/trackfield) | Estratégico |  |
| [Tractian](https://careers.tractian.com/jobs) | Estratégico |  |
| [Tramontina](https://trabalheconosco.vagas.com.br/tramontina) | Estratégico |  |
| [Transperfect Gaming](https://gaming.transperfect.com/careers) | Games |  |
| [Transport NSW](https://jobs.transport.nsw.gov.au/search) | Transporte |  |
| [TransUnion](https://transunion.wd5.myworkdayjobs.com/TransUnion) | Financeiro |  |
| [Traz Pra Mim](https://trabalheconosco.vagas.com.br/trazpramim) | Estratégico |  |
| [Trigg](https://trabalheconosco.vagas.com.br/trigg) | Estratégico |  |
| [Trisul](https://trabalheconosco.vagas.com.br/trisul) | Construção |  |
| [Triunfo Participações](https://trabalheconosco.vagas.com.br/triunfoparticipaes) | Estratégico |  |
| [Trybe](https://betrybe.inhire.app/vagas) | EdTech |  |
| [Uber Brasil](https://www.uber.com/br/pt/careers) | Logística/Delivery |  |
| [Ubisoft](https://www.ubisoft.com/en-us/company/careers) | Jogos |  |
| [Ultrapar](https://trabalheconosco.vagas.com.br/ultrapar) | Energia/Petróleo |  |
| [União Química](https://trabalheconosco.vagas.com.br/unioqumica) | Estratégico |  |
| [Unico](https://unicotech.inhire.app/vagas) | ID Tech |  |
| [Unifique](https://trabalheconosco.vagas.com.br/unifique) | Telecom |  |
| [Unilever](https://careers.unilever.com/en/search-jobs) | Bens de Consumo |  |
| [Unimed (Sistema Nacional)](https://trabalheconosco.vagas.com.br/unimed) | Saúde |  |
| [Unipar Carbocloro](https://trabalheconosco.vagas.com.br/uniparcarbocloro) | Educação |  |
| [United Airlines](https://careers.united.com) | Aviação |  |
| [UP Brasil](https://upbrasil.pandape.infojobs.com.br) | Benefícios |  |
| [Vagas.com](https://vagas.gupy.io) | HR Tech |  |
| [Vale](https://carreiras.gupy.io/vale) | Indústria |  |
| [Vale](https://vale.eightfold.ai/careers?location=Brazil) | Indústria |  |
| [Vasta Educação](https://trabalheconosco.vagas.com.br/vastaeducao) | Educação |  |
| [Veeva](https://veeva.com/careers) | Tecnologia |  |
| [Veloe](https://vagas.veloe.com.br/jobs) | Soluções de Pagamento |  |
| [Verde Campo](https://trabalheconosco.vagas.com.br/verdecampo) | Estratégico |  |
| [Vindi](https://vindi.gupy.io) | Fintech |  |
| [Vinta](https://vinta.inhire.app/vagas) | Tecnologia |  |
| [Visa](https://carreiras.gupy.io/visa) | Financeiro |  |
| [Vitru](https://trabalheconosco.vagas.com.br/vitru) | Estratégico |  |
| [Viver](https://trabalheconosco.vagas.com.br/viver) | Estratégico |  |
| [VLI Logística](https://trabalheconosco.vagas.com.br/vlilogstica) | Logística |  |
| [Volkswagen](https://carreiras.gupy.io/volkswagen) | Automotivo |  |
| [Volvo](https://www.volvogroup.com/en/careers.html) | Automotivo |  |
| [Volvo Infor](https://career55.sapsf.eu/careers?company=volvoinfor) | Automotivo |  |
| [Votorantim S.A.](https://trabalheconosco.vagas.com.br/votorantimsa) | Finanças/Banco & Fintech |  |
| [VR](https://www.portalsinergyrh.com.br/Portal/MeuPortal/MeuPortal?empresa=1581&master=0#suaNovoCarreira) | Benefícios |  |
| [VR Benefícios](https://trabalheconosco.vagas.com.br/vrbenefcios) | Estratégico |  |
| [VTEX](https://job-boards.greenhouse.io/vtex) | Tecnologia |  |
| [Warner Bros. Discovery](https://careers.wbd.com/hbo-jobs) | Entretenimento |  |
| [Warren](https://trabalheconosco.vagas.com.br/warren) | Estratégico |  |
| [Wellhub (GymPass)](https://boards.greenhouse.io/gympass) | Saúde |  |
| [Welocalize](https://jobs.lever.co/welocalize) | Consultoria |  |
| [Westwing](https://trabalheconosco.vagas.com.br/westwing) | Estratégico |  |
| [WeWork](https://wework.wd1.myworkdayjobs.com/WeWork) | Espaços de Trabalho |  |
| [WEX](https://wexinc.wd5.myworkdayjobs.com/WEXInc) | Financeiro |  |
| [Wildlife Studios](https://job-boards.greenhouse.io/wildlifestudios) | Games |  |
| [Wildlife Studios](https://boards.greenhouse.io/wildlifestudios) | Games |  |
| [Wilhelmsen](https://wilhelmsen.wd3.myworkdayjobs.com/Wilhelmsen) | Logística |  |
| [will bank](https://willbank.inhire.app/vagas) | Banco |  |
| [WillowTree](https://willowtreeapps.com/careers) | Tecnologia |  |
| [Wiz Soluções](https://trabalheconosco.vagas.com.br/wizsolues) | Estratégico |  |
| [Wordpress-proxy](https://wordpress-proxy.inhire.com.br) | A Classificar |  |
| [Xometry](https://job-boards.greenhouse.io/xometry) | Tecnologia |  |
| [XP Banco](https://trabalheconosco.vagas.com.br/xpbanco) | Finanças/Banco & Fintech |  |
| [XP Inc](https://boards.greenhouse.io/xpinc) | Financeiro |  |
| [Yorgus](https://trabalheconosco.vagas.com.br/yorgus) | Estratégico |  |
| [Zaffari](https://zaffari.gupy.io) | Varejo |  |
| [Zé Delivery](https://carreiras.gupy.io/zedelivery) | Delivery |  |
| [Zendesk](https://www.zendesk.com.br/company/careers) | Tecnologia |  |
| [Zenir](https://zenir.gupy.io) | Varejo |  |
| [ZF Friedrich](https://career5.successfactors.eu/careers?company=zffriedric) | Automotivo |  |
| [Zoom](https://careers.zoom.us/home) | Tecnologia |  |
| [Zup Innovation](https://job-boards.greenhouse.io/zupinnovation) | Tecnologia |  |
