# Problema 1:
# Dado uma lista de dicionários (chave/valor)Python, verifique se existe a chave 'nome', e caso exista, salve o valor
# dessa chave em uma segunda lista, de modo que não haja repetição de valores na segunda lista.

# Solução:
# 1 - Criar uma lista, com dicionários nomeados dentro dela, dos quais um será a chave nome.
# 2 - Usar uma condicional para verificar se existe a chave nome no dicionário.
# 3 - Quando existir a chave nome no dicionário, enviar o nome digitado para a lista de nomes.
# 4 - Se o nome (valor) já existir na lista mostra a mensagem "já cadastrado".
# 5 - Se o nome não existir na lista mostra a mensagem "cadastrado com sucesso" e adicionar à lista.
# 6 - *Ia ser legal um botão que mostrasse a lista. Mas ainda vou pensar porque isso sai do escopo do projeto
# lista = [{}] #Dicionário de chaves dentro de uma lista.

nomes = []
idades = []
p = 0
dados = {'nome': nomes, 'idade': idades} #1
if 'nome' in dados: #2
      while dados['nome'] == nomes: #3
            n = str(input('Digite o nome:')).upper()
#            idades.append(int(input('Digite a idade: ')))
#            print(nomes)

            if n in nomes: #4
                  print('Nome já cadastrado. Cadastre outro nome.')
            else: #5
                  idades.append(int(input('Digite a idade: ')))
                  print('Cadastrado com sucesso!')
                  nomes.append(n)

            while True: #Confirmação para um nome já cadastrado
                  continuar = str(input('Gostaria de continuar? [S] [N]')).upper()
                  if continuar == 'N':
                        break
                  elif continuar == 'S':
                        break
                  else:
                        print('Opção inválida. Tente novamente')
            if continuar == 'N':
                  break

print(nomes)
