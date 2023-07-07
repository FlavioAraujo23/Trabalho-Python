# Exercicio 2/4 da atividade pratica
print('Bem vindo a lanchonete do Flávio Lopes de Araújo')
print('-------------------CARDÁPIO-------------------')
print('|  Código  |       Descrição       |  Valor  |')
print('|  100     |    Cachorro quente    |   9,00  |')
print('|  101     | Cachorro quente duplo |  11,00  |')
print('|  102     |          X-Egg        |  12,00  |')
print('|  103     |       X-Salada        |  12,00  |')
print('|  104     |        X-Bacon        |  14,00  |')
print('|  105     |         X-Tudo        |  17,00  |')
print('|  200     |   Refrigerante Lata   |   5,00  |')
print('|  201     |       Chá Gelado      |   4,00  |')
print('----------------------------------------------')

# declaração de variaveis
acumulador = 0

# condicionais
while True:
  cod = int(input('Digite o código do produto desejado: '))
  if (cod != 100 and cod != 101 and cod != 102 and cod != 103 and cod != 104 and cod != 105 and cod != 200 and cod != 201):
    print('opção inválida')
    continue
  
  if cod == 100:
   print('Você pediu um Cachorro quente no valor de R$ 9,00 ')
   acumulador += 9
   
  elif cod == 101:
   print('Você pediu um Cachorro quente duplo no valor de R$ 11,00 ')
   acumulador += 11
   
  elif cod == 102:
   print('Você pediu um X-Egg no valor de R$ 12,00 ')
   acumulador += 12
   
  elif cod == 103:
   print('Você pediu um X-Salada no valor de R$ 12,00 ')
   acumulador += 12
   
  elif cod == 104:
   print('Você pediu um X-Bacon no valor de R$ 14,00 ')
   acumulador += 14
   
  elif cod == 105:
   print('Você pediu um X-Tudo no valor de R$ 17,00 ')
   acumulador += 17
   
  elif cod == 200:
   print('Você pediu um Refrigerante Lata no valor de R$ 5,00 ')
   acumulador += 5
   
  elif cod == 201:
   print('Você pediu um Chá Gelado no valor de R$ 4,00 ')
   acumulador += 4
   
# saida de dados 
  pedir_mais = int(input('Deseja pedir mais alguma coisa? \n 1 - Sim \n 2 - Não \n'))
  if pedir_mais == 1:
    continue
  else:
    print('o total a ser pago é R$ {:.2f}'.format(acumulador))
    break