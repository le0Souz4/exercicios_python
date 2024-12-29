"""
Crie um programa que leia o ano de nascimento 
de sete pessoas. No final, mostre quantas pessoas 
ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date  # Importamos a biblioteca datetime para trabalhar com datas

# Definir o ano atual
ano_atual = date.today().year  # Capturamos o ano atual automaticamente

# Inicializamos as variáveis para contagem
maior_idade = 0  # Contará quantas pessoas já atingiram a maioridade
menor_idade = 0  # Contará quantas pessoas ainda não atingiram a maioridade

# Laço para processar os anos de nascimento de 7 pessoas
for pessoa in range(1, 8):  # Repetimos o processo para 7 pessoas
    ano_nascimento = int(input(f"Informe o ano de nascimento da {pessoa}ª pessoa: "))
    idade = ano_atual - ano_nascimento  # Calculamos a idade da pessoa
    
    # Verificar se a pessoa já atingiu a maioridade
    if idade >= 18:  # Consideramos 18 anos como maioridade
        maior_idade += 1  # Incrementamos a contagem de maiores de idade
    else:
        menor_idade += 1  # Incrementamos a contagem de menores de idade

# Mostramos os resultados
print(f"\nTotal de pessoas maiores de idade: {maior_idade}")
print(f"Total de pessoas menores de idade: {menor_idade}")
