""" Crie um programa que leia o nome e o 
preço de vários produtos. O programa deverá 
perguntar se o usuário vai continuar ou não.
No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""

# Inicialização das variáveis
total_gasto = 0
produtos_acima_1000 = 0
produto_mais_barato = ""
preco_mais_barato = float('inf')  # Inicializando com um valor muito alto para garantir que qualquer preço será menor

while True:
    # Leitura do nome e preço do produto
    nome_produto = input("Digite o nome do produto: ").strip()
    preco_produto = float(input(f"Digite o preço do produto {nome_produto}: R$ "))

    # Atualiza o total gasto na compra
    total_gasto += preco_produto

    # Conta quantos produtos custam mais de R$1000
    if preco_produto > 1000:
        produtos_acima_1000 += 1

    # Verifica qual é o produto mais barato
    if preco_produto < preco_mais_barato:
        preco_mais_barato = preco_produto
        produto_mais_barato = nome_produto

    # Pergunta se o usuário deseja continuar
    continuar = input("Você deseja continuar cadastrando produtos? (S para sim, N para não): ").strip().lower()
    if continuar != 's':
        break

# Exibe os resultados finais
print(f"\nA) O total gasto na compra foi: R$ {total_gasto:.2f}")
print(f"B) Quantos produtos custam mais de R$ 1000: {produtos_acima_1000}")
print(f"C) O produto mais barato foi: {produto_mais_barato} que custa R$ {preco_mais_barato:.2f}")
