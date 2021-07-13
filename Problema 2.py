# Problema 2:
# Dado um arquivo csv com delimitador ';' e com o seguinte cabeçalho: id;nome;telefone;idade.
# * Retorne uma lista com os registros ordenados por nome.
# * Exemplo de arquivo:
# * Id;nome;telefone;idade
# * 1;João;43383832;28
# * 2;Maria;43839322;32
# * .
# * .
# * .
# * N;Zzzz;99999999;12'''

# Solução:
# 1 - Abrir um arquivo csv pelo python.
# 2 - Ajustar o delimitador para ";".
# 3 - Montar o cabeçalho como o do exemplo.
# 4 - Organizar a lista por ordem alfabética.
# 5 - Mostrar a lista organizada.

import csv
import operator

print(f'|{"id":3}|{"Nome":25}|{"Telefone":15}|{"Idade":5}|')#3
with open('Dados.csv') as dadoscsv: #1
    dadoscsv = csv.reader(dadoscsv, delimiter=';')#2
    dadoscsv.__next__()
    ordem = sorted(dadoscsv, key=operator.itemgetter(1))#4
    for row in ordem:#5
        print(f'|{row[0]:3}|{row[1]:25}|{row[2]:15}|{row[3]:5}|')
