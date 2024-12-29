"""
 Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros
"""

# Entrada do preço do produto e da condição de pagamento
preco = float(input("Digite o preço do produto: R$ "))
print("Escolha a forma de pagamento:")
print("[1] À vista (dinheiro/cheque)")
print("[2] À vista (no cartão)")
print("[3] Em até 2x no cartão")
print("[4] 3x ou mais no cartão")

condicao_pagamento = int(input("Digite a opção de pagamento: "))

# Cálculos baseados na condição de pagamento
if condicao_pagamento == 1:
    # À vista (dinheiro/cheque): 10% de desconto
    preco_final = preco - (preco * 0.10)
    print(f"Você pagará R$ {preco_final:.2f} com 10% de desconto.")
elif condicao_pagamento == 2:
    # À vista (no cartão): 5% de desconto
    preco_final = preco - (preco * 0.05)
    print(f"Você pagará R$ {preco_final:.2f} com 5% de desconto.")
elif condicao_pagamento == 3:
    # Em até 2x no cartão: preço normal
    print(f"Você pagará R$ {preco:.2f} em até 2x no cartão sem juros.")
elif condicao_pagamento == 4:
    # 3x ou mais no cartão: 20% de juros
    preco_final = preco + (preco * 0.20)
    print(f"Você pagará R$ {preco_final:.2f} com 20% de juros.")
else:
    print("Opção inválida. Por favor, escolha uma opção de pagamento válida.")
