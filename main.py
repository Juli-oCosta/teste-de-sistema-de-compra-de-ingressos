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
    subtotal = sum(ingresso['valor'] for ingresso in compra)
    quantidade_total = len(compra)
    desconto_aplicado = 0

    print("\n" + "="*30)
    print("      RESUMO DA COMPRA")
    print("="*30)

    print("Itens Comprados:")
    for ingresso in compra:
        print(f"- 1x Ingresso {ingresso['tipo']} ({ingresso['categoria']}): R$ {ingresso['valor']:.2f}")

    print("-"*30)
    
    print(f"Subtotal: R$ {subtotal:.2f}")
    print(f"Total de Ingressos: {quantidade_total}")

    if quantidade_total >= REGRAS_DESCONTO['QUANTIDADE_MINIMA']:
        desconto_aplicado = subtotal * REGRAS_DESCONTO['PERCENTUAL']
        print(f"Desconto Aplicado ({REGRAS_DESCONTO['PERCENTUAL']*100:.0f}%): -R$ {desconto_aplicado:.2f}")

    total_final = subtotal - desconto_aplicado

    print("-"*30)
    print(f"TOTAL A PAGAR: R$ {total_final:.2f}")
    print("="*30)


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
