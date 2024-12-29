"""
Desenvolva um programa que leia o nome, idade e sexo 
de 4 pessoas. No final do programa, mostre: a média 
de idade do grupo, qual é o nome do homem mais velho 
e quantas mulheres têm menos de 20 anos.
"""

# Inicializamos as variáveis necessárias
soma_idades = 0  # Para somar as idades
maior_idade_homem = 0  # Para armazenar a idade do homem mais velho
nome_homem_mais_velho = ''  # Para armazenar o nome do homem mais velho
contagem_mulheres_menores_20 = 0  # Contador para mulheres com menos de 20 anos

# Laço para processar os dados de 4 pessoas
for i in range(1, 5):  # O laço vai de 1 até 4, ou seja, 4 iterações
    print(f"Dados da {i}ª pessoa:")
    nome = input("Nome: ")  # Leitura do nome
    idade = int(input("Idade: "))  # Leitura da idade
    sexo = input("Sexo (M/F): ").lower()  # Leitura do sexo, convertendo para minúsculo para padronização
    
    # Soma das idades para cálculo da média
    soma_idades += idade
    
    # Verificação do homem mais velho
    if sexo == 'm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_mais_velho = nome
    
    # Verificação de mulheres com menos de 20 anos
    if sexo == 'f' and idade < 20:
        contagem_mulheres_menores_20 += 1

# Cálculo da média de idade
media_idade = soma_idades / 4

# Exibindo os resultados
print(f"\nMédia de idade do grupo: {media_idade:.2f} anos")
print(f"O homem mais velho é {nome_homem_mais_velho} com {maior_idade_homem} anos.")
print(f"Quantidade de mulheres com menos de 20 anos: {contagem_mulheres_menores_20}")
