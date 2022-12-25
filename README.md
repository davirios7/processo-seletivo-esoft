# Processo Seletivo para E-soft sistema Ltda.
Teste prático – Projeto em Django

Faça um sistema onde terá um cadastro de pessoas, utilizando a linguagem de
programação Python, e o framework Django. O sistema terá as seguintes telas --- foi adicionado uma terceira tela para edição de usuários --- :

1. Tela de listagem de pessoas cadastradas:
  1.1. Mostrará uma tabela contendo as pessoas cadastradas no banco de dados ✔️
  
  1.2. Preencher a tabela em ordem alfabética, considerando o campo nome, seguido do campo sobrenome. A ordenação deve ser crescente ✔️
  
  1.3. Terá um botão chamado “cadastrar”, onde será redirecionado para a página do cadastro de pessoas ✔️

2. Tela de cadastro de pessoas:

  2.1. Terá um formulário com os campos: nome, sobrenome, idade, data de nascimento, e-mail, apelido e observação; ✔️
  
  2.2. Os campos nome, sobrenome, idade, data de nascimento e e-mail são obrigatórios; ✔️
  
  2.3. Os campos nome e o sobrenome deverão ser gerados de forma aleatória. Para isso, utilize a api de geradores de nomes aleatórios (disponível em https://gerador-nomes.herokuapp.com); ✔️ --- o link não estava funcionando, então utilizei outra api (https://gerador-nomes.wolan.net) ---
  
  2.4. Exemplo de uso da api de geração de nomes aleatórios: https://gerador-nomes.herokuapp.com/nome/aleatorio; --- Não foi possível visualizar também ---

  2.5. Ao obter os dados do nome e sobrenome, preencher automaticamente o formulário, com os valores correspondentes. Os valores nome e sobrenome, que vem da consulta da api, deverão ser salvos no campo nome; ✔️ -- Não entendi ao certo se o nome e sobrenome deveriam preencher os dois campos, mas como foi pedido preencher somento o campo "nome", foi o que fiz ---
  
  2.6. Terá um botão “cadastrar”, onde serão gravados os dados da pessoa no banco de dados. Caso a gravação seja feita com sucesso, redirecionar para a página de listagem de pessoas; ✔️
  
  2.7. Permitir a edição dos dados de uma pessoa cadastrada no sistema; ✔️ --- feito na terceira tela ---
  
  2.8. Esta será a tela inicial do sistema; ✔️


Observações:
1. Pode-se utilizar qualquer gerenciador de banco de dados, que seja suportado pelo
framework Django; ✔️ Utilizado: MYSQL
2. O sistema pode ser feito utilizando as versões 2.7 e 3.x, do Python; ✔️
3. O projeto deve ser enviado para um repositório do GitHub, bem como o arquivo
com a estrutura do banco de dados (arquivo sql ou sqlite), e demais informações
ou comentários acerca do sistema; ✔️
4. Fique a vontade para utilizar quaisquer bibliotecas, plugins ou complementos para
Javascript, css e Python; ✔️ Foi utilizado Javascript, Jquery, dentre outros para melhorias no sistema.
5. O link do repositório no GitHub deverá ser enviado por e-mail ✔️

AVISO: DEIXEI O PYTHON INTREPETER SEM SER MODIFICADO (DA MANEIRA QUE USEI COM AS CONFIGURAÇÕES DA MINHA MAQUINA) POIS NÃO SABIA AO CERTO COMO QUERIAM, ENTÃO PRESUMO QUE O AMBIENTE VIRTUAL SERÁ CRIADO POR QUEM IRÁ ANALISAR O PROJETO.

Agradeço novamento pela oportunidade!! :D
