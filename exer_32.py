"""
Faça um programa que leia três números e
 mostre qual é o maior e qual é o menor.
"""

num1 = int(input("digite o primeiro numero: \n"))
num2 = int(input("digite o segundo número: \n"))
num3 = int(input("digite o terceiro numero: \n"))
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print(f"o menor valor foi {menor}")
print(f'e o maior valor foi {maior}')
