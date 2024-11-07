""" crie um algoritimo que leia um numero
e mostre o seu dobro, triplo e raiz quadrada"""
#forma simples
num1 = int(input('Digite um numero: '))
dob = num1 * 2
tri = num1 * 3
rzq = num1 ** (1/2)

print(f"o numero escolhido foi {num1},"
      f"\n Seu dobro é {dob}, seu triplo é {tri}"
      f"\n e sua raiz quadrada {rzq:.2f}")