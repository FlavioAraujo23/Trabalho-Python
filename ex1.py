# Exercicio 1/4 da atividade pratica
# Entrada de dados
print('Bem vindo a loja do Flávio Lopes de Araújo')
produto_valor = float(input('Digite o valor do produto: '))
qtd_produto = int(input('Digite a quantidade de produto: '))


# Condicionais
total = produto_valor * qtd_produto

if qtd_produto <= 9:
  desconto = 0
  d = 0

elif qtd_produto >= 10 and qtd_produto <= 99:
  desconto = total * 0.5
  d = 5
  
elif qtd_produto >= 100 and qtd_produto <= 999: 
  desconto = total * 0.10
  d = 10
  
else: 
  qtd_produto >= 1000
  desconto = total * 0.15
  d = 15
  
valor_desconto = total - desconto

# Saída de dados
print('o valor sem desconto foi: R${:.2f}'.format(total))
print('o valor com desconto foi: R${:.2f}    (desconto {}%)'.format(valor_desconto, d))