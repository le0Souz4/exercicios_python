"""
Faça um programa que tenha uma função chamada área()
que receba as dimensões de um terreno retangular e mostre a
área deste terreno
"""

def area(comp, larg):  # Define a função 'area' que recebe dois parâmetros: comprimento (comp) e largura (larg)
    area_ret = comp * larg  # Calcula a área do terreno (comprimento × largura)
    print(f'A área do terreno é de {area_ret}m²')  # Exibe a área calculada, formatada em metros quadrados

# Solicita ao usuário a largura do terreno
largura = float(input("Digite a largura: "))  
# Solicita ao usuário o comprimento do terreno
comprimento = float(input("Digite o comprimento: "))

# Chama a função 'area' passando os valores fornecidos pelo usuário como argumentos
area(largura, comprimento)
