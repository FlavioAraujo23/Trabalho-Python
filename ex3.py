# Exercicio 3/4 da atividade pratica

# inicio da função dimensoesObjeto()
def dimensoesObjeto():
  while True:
    try:
      altura = float(input("Digite a altura do objeto em cm: "))
      comprimento = float(input("Digite o comprimento do objeto em cm: "))
      largura = float(input("Digite a largura do objeto em cm: "))
      volume = altura * comprimento * largura
      print(f'o volume do objeto é (em cm): {volume}')
      if volume < 1000:
        valor = 10
      elif 1000 <= volume < 10000:
        valor = 20
      elif 10000 <= volume < 30000:
        valor = 30
      elif 30000 <= volume < 100000:
        valor = 50
      elif volume >= 100000:
        print("Este volume de 100000 cm³ é muito grande e não aceitamos. \n Por favor, digite um valor válido.\n")
        continue
      return valor
    except ValueError:
        print("Valor inválido. Por favor, digite um valor numérico.\n")
        continue

# fim da função dimensoesObjeto()

# inicio da função pesoObjeto()
def pesoObjeto():
  while True:
    try:
      peso = float(input("Qual é o peso do objeto (em kg)? "))
      if peso <= 0.1:
        multiplicador = 1
      elif 0.1 <= peso < 1:
        multiplicador = 1.5
      elif 1 <= peso < 10:
        multiplicador = 2
      elif 10 <= peso < 30:
        multiplicador = 3
      elif peso >= 30:
        print("O peso máximo permitido é de 30kg. Por favor, digite um valor válido.\n")
        continue
      return multiplicador
    except ValueError:      
        print("Valor inválido. Por favor, digite um valor numérico.\n")
        continue
# fim da função pesoObjeto()

# inicio da função rotaObjeto()
def rotaObjeto():
    while True:
        rota = input("Selecione a rota: \n RS - De Rio de Janeiro até São Paulo \n SR - De São Paulo até Rio de Janeiro \n BS - De Brasília até São Paulo \n SB - De São Paulo até Brasília \n BR - De Brasília até Rio de Janeiro \n RB - Rio de Janeiro até Brasília \n Digite a sigla correspondente (RS, SR, BS, SB, BR ou RB): ").lower()
        if rota == "rs" or rota == "sr":
            multiplicador = 1
        elif rota == "bs" or rota == "sb":
            multiplicador = 1.2
        elif rota == "br" or rota == "rb":
            multiplicador = 1.5
        else:
            print("Rota inválida. Por favor, digite uma rota válida.\n")
            continue
        
        print(f"O multiplicador para essa rota é de {multiplicador}.")
        return multiplicador

# fim da função rotaObjeto()

# inicio do main
print('Bem Vindo a Companhia de Logistica Flávio Lopes de Araújo S.A.')
volume = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = (volume * peso) + rota
  
print ('Total a pagar: R$ {}      (dimensoes {} * peso {} * rota {})'.format(total, volume, peso, rota))