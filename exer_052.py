"""
Crie um programa que leia uma frase qualquer 
e diga se ela é um palíndromo, desconsiderando os 
espaços.
"""

# Solicita ao usuário que insira uma frase qualquer
frase = input("Digite uma frase para verificar se é um palíndromo: ").strip().upper()
# .strip() remove espaços no início e no fim da frase
# .upper() converte a frase para letras maiúsculas para evitar diferenças de caso (ex.: 'a' e 'A')

# Remove os espaços internos da frase e cria uma string contínua
frase_junta = ''.join(frase.split())
# .split() divide a frase em uma lista de palavras, separando pelos espaços
# .join() junta as palavras da lista em uma única string, removendo todos os espaços

# Verifica se a frase sem espaços é igual à sua versão invertida
if frase_junta == frase_junta[::-1]:
    # A sintaxe [::-1] inverte a string
    print(f"A frase '{frase}' é um palíndromo!")
    # Se a string original sem espaços for igual à invertida, é um palíndromo
else:
    print(f"A frase '{frase}' NÃO é um palíndromo.")
    # Caso contrário, a frase não é um palíndromo
