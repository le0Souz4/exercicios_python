"""
Crie um programa que leia vários números e
coloca em uma lista. Depois disso, mostre:
-> Quantos números foram digitados;
-> A lista de valores, ordenada de forma decrescente
-> Se o valor 5 foi digitado e está ou não na lista
"""

valores = list()
posicao = 1
while True:
    valores.append(int(input(f' por favor digite o {posicao}° número: ')))
    posicao += 1
    dec = input('deseja continuar? [S] // [N]').strip().upper()[0]
    if dec == "N":
        break
valores.sort(reverse=True)
print(f'Você digitou um total de {len(valores)} numeros;'
      f'\na lista em ordem decrescente fica: {valores}')
if 5 in valores:
    print(f'você digitou {valores.count(5)}x o número 5')
else:
    print('Você não digitou nenhuma vez o numero 5')
