"""
Desenvolva um programa que leia o comprimento de 
três retas e diga ao usuário se elas podem ou não 
formar um triângulo.
"""

# Solicita os comprimentos das três retas
reta1 = float(input("Digite o comprimento da primeira reta: "))
reta2 = float(input("Digite o comprimento da segunda reta: "))
reta3 = float(input("Digite o comprimento da terceira reta: "))

# Verifica a condição de existência de um triângulo
if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print("As retas informadas PODEM formar um triângulo!")
else:
    print("As retas informadas NÃO PODEM formar um triângulo.")
