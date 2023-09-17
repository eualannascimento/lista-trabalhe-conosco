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

| Nome da Empresa (+ Link do Trabalhe Conosco) |
| --- |
| [3M](https://3m.wd1.myworkdayjobs.com/pt-BR/Search) |
| [Accenture](https://www.accenture.com/pt-pt/careers/jobsearch?clp=1&jk=&sb=1&pg=1&vw=1&is_rj=0) |
| [Adobe](https://careers.adobe.com/us/en/c/other-jobs) |
| [Agi](https://agibank.gupy.io/) |
| [Alelo](https://vagas.alelo.com.br/jobs) |
| [Alura](https://grupoalura.gupy.io/) |
| [Ambev](https://ambev.gupy.io/) |
| [Ambev Tech](https://ambevtech.gupy.io/) |
| [ANBIMA](https://anbima.gupy.io/) |
| [Banco ABC](https://abcbrasil.gupy.io/) |
| [Banco BV](https://jobs.lever.co/bv) |
| [Banco Daycoval](https://bancodaycoval.gupy.io/) |
| [Banco Fibra](https://bancofibra.gupy.io/) |
| [Banco Master](https://bancomaster.gupy.io/) |
| [Banco Mercantil](https://mercantil.gupy.io/) |
| [Banco Ourinvest](https://bancoourinvest.gupy.io) |
| [Banco Pan](https://boards.greenhouse.io/bancopan) |
| [Banco Rodobens](https://rodobenscarreiras.gupy.io/) |
| [Banco Sofisa](https://bancosofisa.gupy.io/) |
| [banQi](https://banqi.gupy.io/) |
| [BMG](https://bmg.gupy.io/) |
| [BMW Group Brasil](https://bmw.gupy.io/) |
| [Brasilprev](https://brasilprev.gupy.io/) |
| [C&A](https://cea.gupy.io/) |
| [C6 Bank](https://boards.greenhouse.io/c6bank) |
| [Cacau Show](https://cacaushow.gupy.io/) |
| [Centauro](https://centaurotalentos.gupy.io/) |
| [Cielo](https://cielo.gupy.io/) |
| [ClearSale](https://clearsale.gupy.io/) |
| [Coca-Cola Company](https://coke.wd1.myworkdayjobs.com/coca-cola-careers/) |
| [Coca-Cola FEMSA Brasil](https://trabalheconosco.vagas.com.br/femsa/oportunidades) |
| [Colgate-Palmolive](https://jobs.colgate.com/go/View-All-Jobs/8506400/) |
| [Creditas (Internacional)](https://boards.greenhouse.io/creditasen) |
| [Creditas (Nacional)](https://boards.greenhouse.io/creditas) |
| [CVC Corp](https://cvccorp.gupy.io/) |
| [CVP (Caixa Vida e Previdência)](https://caixavidaeprevidencia.gupy.io/) |
| [Dasa Tecnologia](https://dasatecnologia.gupy.io/) |
| [DiDi (99)](https://careers-didiglobal.icims.com/jobs/search?ss=1&hashed=-625919479) |
| [Digio](https://digio.gupy.io/) |
| [Dotz](https://dotz.gupy.io/) |
| [Ebanx](https://boards.greenhouse.io/ebanx) |
| [Elo](https://vempraelo.gupy.io/) |
| [Embraer](https://embraer.gupy.io/) |
| [EMS](https://ems.gupy.io/) |
| [Energisa (Corp)](https://grupoenergisa.gupy.io/) |
| [Energisa (Tecnologia)](https://energisatech.gupy.io/) |
| [FGV - Fundação Getulio Vargas](https://trabalheconosco.fgv.br/vagas) |
| [Genial Investimentos](https://genial.gupy.io/) |
| [Getnet](https://getnet.gupy.io/) |
| [Globo](https://globo.gupy.io/) |
| [GOL Linhas Aéreas](https://golcarreiras.gupy.io/) |
| [GPA](https://digitalgpa.gupy.io/) |
| [Grupo Boticário](https://grupoboticario.gupy.io/) |
| [Grupo Carrefour](https://corporativo-grupocarrefourbrasil.pandape.infojobs.com.br/) |
| [Grupo L'Occitane](https://sejaloccitane.gupy.io/) |
| [Gupy](https://vempra.gupy.io/) |
| [Hering](https://ciahering.gupy.io/) |
| [Hotmart](https://boards.eu.greenhouse.io/hotmartcareersbr) |
| [Intel](https://jobs.intel.com/en/search-jobs?k=&l=&orgIds=599) |
| [Itaú](https://vemproitau.gupy.io/) |
| [KPMG Brasil](https://kpmgbrasil.gupy.io/) |
| [Livelo](https://livelo.gupy.io/) |
| [Localiza](https://localiza.gupy.io/) |
| [Loggi](https://apply.workable.com/loggi) |
| [MadeiraMadeira](https://madeiracarreira.gupy.io/) |
| [McDonalds (Corporativo)](https://corporativomc.gupy.io/) |
| [McDonalds (Restaurante)](https://restaurantemc.gupy.io/) |
| [Meliuz](https://meliuz.gupy.io/) |
| [Microsoft](https://careers.microsoft.com/us/en/search-results) |
| [MJV](https://mjvcarreiras.gupy.io/) |
| [Natura&CO (Avon + The Body Shop)](https://avon.wd5.myworkdayjobs.com/NaturaAndCoCareers) |
| [Neon](https://jobs.lever.co/neon) |
| [Notion](https://boards.greenhouse.io/notion) |
| [Nubank](https://boards.greenhouse.io/nubank) |
| [PagSeguro](https://pagseguro.gupy.io/) |
| [Paschoalotto](https://paschoalotto.gupy.io/) |
| [Pede Pronto](https://jobs.pedepronto.com.br/jobs) |
| [Porto](https://porto.gupy.io/) |
| [Positivo Tecnologia](https://positivotecnologia.gupy.io/) |
| [Quinto Andar](https://apply.workable.com/quintoandar/) |
| [QUOD](https://vempraquod.gupy.io/) |
| [Raizen](https://genteraizen.gupy.io/) |
| [RecargaPay](https://apply.workable.com/recargapay/) |
| [Record](https://recordtv.gupy.io/) |
| [Rede](https://vemprarede.gupy.io/) |
| [Safra](https://venhasersafra.gupy.io/) |
| [Santander](https://santanderbrasil.gupy.io/) |
| [Sicredi](https://sicredi.gupy.io/) |
| [Sinch](https://apply.workable.com/sinch/) |
| [TakeBlip](https://takeblip.gupy.io/) |
| [TIVIT](https://tivit.gupy.io/) |
| [Toyota Brasil](https://toyotabrasil.gupy.io/) |
| [Unimed Brasil](https://unimed-brasil.gupy.io/) |
| [Veloe](https://vagas.veloe.com.br/jobs) |
| [Via](https://viavarejo.gupy.io/) |
| [Via (Corporativo)](https://corporativovia.gupy.io/) |
| [Via (HUB)](https://viahub.gupy.io/) |
| [Vivo](https://vivo.gupy.io/) |
| [Vivo Digital](https://vivodigital.gupy.io/) |
| [VR](https://vr.gupy.io/) |
| [will bank](https://vemserwill.gupy.io/) |
| [XP Inc](https://boards.greenhouse.io/xpinc) |
