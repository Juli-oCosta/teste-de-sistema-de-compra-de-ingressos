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
  return 0

def comprar_ingresso():
  print("Bem vindo à nossa bilheteria!!")
  print()

  carrinho_de_compras = []

  while True:
    try:
      qtd_ingresso = int(input("Digite a quantidade de ingressos que deseja comprar: "))
      if qtd_ingresso > 0: 
        break
      else:
        print("A quantidade de ingressos deve ser maior que zero.")
    except ValueError:
      print("Entrada inválida. Por favor, digite um número inteiro.")

  for i in range(qtd_ingresso):
    print(f"\nAdicionando Ingresso {i+1} de {qtd_ingresso}")

    while True:
      try:
        tipo_ingresso_input = input("Escolha o tipo do ingresso (VIP/Normal): ").upper()
      if tipo_ingresso_input in VALORES_BASE:
        tipo_ingresso = tipo_ingresso_input
        break
      else:
        print("Por favor, digite um tipo válido.")

    while True:
      try:
        categoria_ingresso_iput = input("Escolha a categoria (Inteira/Meia): ").upper()
      if categoria_ingresso_input in ['INTEIRA', 'MEIA']:
        categoria_ingresso = categoria_ingresso_input
        break
      else:
        print("Por favor, digite uma categoria válida.")
    # Valor

    ingresso_atual = {
        "tipo": tipo_ingresso,
        "categoria": categoria_ingresso,
        "valor": c
    }
    carrinho_de_compras.append(ingresso_atual)
