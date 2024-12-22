"""faça um algoritmo que leia o preço de um produto
e mostre o preço com 5% de desconto"""

# Solicita ao usuário o preço original do produto e converte a entrada para número decimal (float)
preco1 = float(input("informe o preço do produto: R$ "))

# Calcula o novo preço após um reajuste de 5%. 
# A operação 'preco1 * 0.05' calcula 5% do preço original, que é subtraído de 'preco1' para aplicar o reajuste
preco2 = preco1 - (preco1 * 0.05)

# Exibe o novo preço do produto após o reajuste de 5%, formatando o valor com 2 casas decimais
print(f"O preço teve um reajuste de 5%, portanto"
      f"\nO novo preço será {preco2:.2f}")
