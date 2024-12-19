"""
Faça um programa que tenha uma função chamada área()
que receba as dimensões de um terreno retangular e mostre a
área deste terreno
"""

def area(comp, larg):
    area_ret = comp * larg
    print(f'A área do terreno é de {area_ret}m²')

largura = float(input("digite a largura"))
comprimento = float(input("digite o comprimento"))

area(largura, comprimento)