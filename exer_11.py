"""faça um algoritmo que leia o preço de um produto
e mostre o preço com 5% de desconto"""
preco1 = float(input("informe o preço do produto: R$ "))
preco2 = preco1 - (preco1 * 0.05)
print(f"O preço teve um reajuste de 5%, portanto"
      f"\nO novo preço será {preco2:.2f}")