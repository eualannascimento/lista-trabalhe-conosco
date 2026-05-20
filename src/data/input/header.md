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