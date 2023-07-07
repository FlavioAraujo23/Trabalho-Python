# Exercicio 4/4 da atividade pratica

#---------- Inicio das Variáveis Globais ---------
lista_produto = []
codigo_produto = 0
#----------   fim das Variáveis Globais  ---------

#---------- Inicio de cadastrar_produto ---------
def cadastrar_produto(codigo):
  print('Bem vindo ao menu de Cadastrar Produto')
  print('Código do Produto {}'.format(codigo))
  nome = input('Entre com o NOME da peça: ')
  fabricante = input('Entre com o FABRICANTE da peça: ')
  preco = int(input('Entre com o PREÇO(R$) da peça: '))
  dicionario_produto = {'codigo'      : codigo,
                         'nome'       : nome,
                         'fabricante' : fabricante,
                         'preco'      : preco}
  lista_produto.append(dicionario_produto.copy())
#----------  fim de cadastrar_produto  ---------

#---------- Inicio de consultar_produto ---------
def consultar_produto():
  print('Bem vindo ao menu de Consultar Produto')
  while True:
    opcao_consultar = input('Escolha a opção desejada:\n'+
                              '1 - Consultar todas as Peças\n'+
                              '2 - Consultar Peças por CÓDIGO\n'+
                              '3 - Consultar Peças por FABRICANTE\n'+
                              '4 - Retornar\n'+
                              '>>')
    if opcao_consultar == '1':
      print('Você selecionou a opção consultar TODOS os produtos')  
      for peca in lista_produto:
        print('----------------------')
        for key, value in peca.items():
          print('{} : {}'.format(key, value))
        print('----------------------')  
    elif opcao_consultar == '2':
      print('Você selecionou a opção consultar Peças por CÓDIGO')
      valor_desejado = int(input('Entre com o CÓDIGO desejado: '))
      for peca in lista_produto:
        if peca['codigo'] == valor_desejado:
          print('----------------------')
          for key, value in peca.items():
            print('{} : {}'.format(key, value))
          print('----------------------')     
    elif opcao_consultar == '3':
      print('Você selecionou a opção consultar Peças por FABRICANTE')  
      valor_desejado = input('Entre com o FABRICANTE desejado: ')
      for peca in lista_produto:
        if peca['fabricante'] == valor_desejado:
          print('----------------------')
          for key, value in peca.items():
            print('{} : {}'.format(key, value))
          print('----------------------')      
    elif opcao_consultar == '4':
      return 
    else:
      print('opção invalida, Tente novamente')
      continue
  
#----------  fim de consultar_produto  ---------

#---------- Inicio de remover_produto ---------
def remover_produto():
  print('Bem vindo ao menu de Remover Produto')
  valor_desejado = int(input('Entre com o CÓDIGO do produto que deseja remover: '))
  for peca in lista_produto:
    if peca['codigo'] == valor_desejado:
      lista_produto.remove(peca)
      print('Produto Removido')
  
#----------  fim de remover_produto  ---------

#---------- Inicio de Main ---------
print('Bem Vindo ao Controle de Estoque da Bicicletaria do Flávio Lopes de Araújo ')
while True:
  opcao_principal = input('Escolha a opção desejada:\n'+
                           '1 - Cadastrar Peças\n'+
                           '2 - Consultar Peças\n'+
                           '3 - Remover Peças\n'+
                           '4 - Sair\n'+
                           '>>')
  if opcao_principal == '1':
    codigo_produto += 1
    cadastrar_produto(codigo_produto)
  elif opcao_principal == '2':
    consultar_produto()
  elif opcao_principal == '3':
    remover_produto()
  elif opcao_principal == '4':
    break
  else:
    print('opção invalida, Tente novamente')
    continue
#----------  fim de Main  ----------