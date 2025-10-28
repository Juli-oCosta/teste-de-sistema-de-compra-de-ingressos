# Utilizando constantes para ter um melhor controle desses valores
VALORES_BASE = {
    'VIP': 300.00,
    'NORMAL': 150.00
}
REGRAS_DESCONTO = {
    'QUANTIDADE_MINIMA': 4,
    'PERCENTUAL': 0.10
}

def calcular_valor_ingresso(tipo, categoria):
  valor = VALORES_BASE[tipo]
  if categoria == 'MEIA':
    valor *= 0.5 # Convertendo valor para a metade do valor cheio
  return valor

def exibir_compra(compra):
  print(compra)

def comprar_ingresso():
  print("Bem vindo à nossa bilheteria!!")
  print()

  carrinho_de_compras = []

  while True:
    try:
      qtd_ingresso = int(input("Digite a quantidade de ingressos que deseja comprar: "))
      if qtd_ingresso >= 0: 
        break
      else:
        print("Por favor, digite uma quantidade válida.")
    except ValueError:
      print("Entrada inválida. Por favor, digite um número inteiro.")

  for i in range(qtd_ingresso):
    print(f"\nAdicionando Ingresso {i+1} de {qtd_ingresso}")

    while True:
      tipo_ingresso_input = input("Escolha o tipo do ingresso (VIP/Normal): ").upper()
      if tipo_ingresso_input in VALORES_BASE:
        tipo_ingresso = tipo_ingresso_input
        break
      else:
        print("Por favor, digite um tipo válido.")

    while True:
      categoria_ingresso_input = input("Escolha a categoria (Inteira/Meia): ").upper()
      if categoria_ingresso_input in ['INTEIRA', 'MEIA']:
        categoria_ingresso = categoria_ingresso_input
        break
      else:
        print("Por favor, digite uma categoria válida.")

    valor_ingresso = calcular_valor_ingresso(tipo_ingresso, categoria_ingresso)

    ingresso_atual = {
        "tipo": tipo_ingresso,
        "categoria": categoria_ingresso,
        "valor": valor_ingresso
    }
    carrinho_de_compras.append(ingresso_atual)

    print(f"Ingresso {tipo_ingresso} ({categoria_ingresso}) adicionado! Valor: R${valor_ingresso:.2f}")
 
  if carrinho_de_compras:
      exibir_compra(carrinho_de_compras)
  else:
      print("\nNenhum ingresso foi comprado. Obrigado pela visita!")

comprar_ingresso()
