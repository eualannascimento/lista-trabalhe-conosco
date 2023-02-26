## 📚 Introdução
O objetivo deste repositório é facilitar o acesso e a busca por oportunidades de trabalho em diferentes empresas, centralizando as plataformas em um só lugar.  
Sinta-se à vontade para contribuir adicionando ou atualizando a lista de empresas.  
Este repositório contém uma lista com: 
- Data de Referência (ou seja, quando entrou na lista);
- Nome da empresa;
- Segmento de atuação;
- Plataforma para processo seletivo;
- Link para acesso ao site.
<br><br>  
## 🔧 Processo
O processo de atualização do README.md para acesso rápido é automatizado por meio do GitHub Actions.  
O fluxo de trabalho 'build-readme.yml', é executado sempre que houver um push na branch main.  
Este fluxo de trabalho executa o script.py, que lê o arquivo 'data/header.md' e o 'data/companies.csv', ordena os dados por data de referência e escreve o arquivo README.md com as informações atualizadas.
<br><br>
## 🤝 Como contribuir
1. Faça um fork do repositório do projeto;
2. Abra o arquivo 'data/companies.csv' e faça suas contribuições (adicionando ou editando);
3. Salve o arquivo 'data/companies.csv' com as alterações.
4. Faça o commit e o push para o seu repositório forkado.
5. Abra um pull request (PR) para o repositório original do projeto, especificando que deseja adicionar ou editar empresas.
6. Aguarde a revisão do PR (possíveis solicitações de alteração) e a eventual aprovação e merge.
<br><br>
## 🏢 Acesso rápido
Para obter todas as informações disponíveis, basta baixar o arquivo 'data/companies.csv'.  
Essa tabela contém somente o nome da empresa com link para o site, visando facilitar o uso via mobile.
<br>