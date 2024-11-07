"""Faça um programa que leia um numero inteiro
e mostre na tela seu sucessor e seu antecessor"""

num = int(input("Digite um numero: "))
ant = num - 1
suc = num + 1
print(f"o numero digitado foi {num}, seu sucessor é {suc} e seu antecessor {ant}")

#tambem pode ser feito da seguinte maneira

num2 = int(input("Digite outro numero: "))
print(f"o numero escolhido foi {num2}, seu sucessor é {num2+1} e seu antecessor {num2-1}")