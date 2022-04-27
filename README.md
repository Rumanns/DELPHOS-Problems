## Aqui resolvemos dois problemas, um sobre registro e outro sobre CSV e como usar CSV;

### Problema 1:
Dado uma lista de dicionários (chave/valor)Python, verifique se existe a chave 'nome', e caso exista, salve o valor
dessa chave em uma segunda lista, de modo que não haja repetição de valores na segunda lista.

Solução:
1 - Criar uma lista, com dicionários nomeados dentro dela, dos quais um será a chave nome.
2 - Usar uma condicional para verificar se existe a chave nome no dicionário.
3 - Quando existir a chave nome no dicionário, enviar o nome digitado para a lista de nomes.
4 - Se o nome (valor) já existir na lista mostra a mensagem "já cadastrado".
5 - Se o nome não existir na lista mostra a mensagem "cadastrado com sucesso" e adicionar à lista.
6 - *Ia ser legal um botão que mostrasse a lista. Mas ainda vou pensar porque isso sai do escopo do projeto
lista = [{}] #Dicionário de chaves dentro de uma lista.

## Problema 2:
Dado um arquivo csv com delimitador ';' e com o seguinte cabeçalho: id;nome;telefone;idade.
* Retorne uma lista com os registros ordenados por nome.
* Exemplo de arquivo:
* Id;nome;telefone;idade
* 1;João;43383832;28
* 2;Maria;43839322;32
* .
* .
* .
* N;Zzzz;99999999;12'''

### Solução:
1 - Abrir um arquivo csv pelo python.
2 - Ajustar o delimitador para ";".
3 - Montar o cabeçalho como o do exemplo.
4 - Organizar a lista por ordem alfabética.
5 - Mostrar a lista organizada.
