'''
Crie um programa que leia vários números e coloque em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os
valores pares e valores impares digitados, respectivamente.
Ao final, mostre o conteúdo das três lsitas geradas
'''

valores = list()
valor_par = list()
valor_impar = list()
pos = 1
while True:
    entrada = int(input(f"por favor digite o {pos}° valor"))
    pos += 1
    valores.append(entrada)
    if entrada % 2 == 0:
        valor_par.append(entrada)
    else:
        valor_impar.append(entrada)
    dec = input('Deseja contiunuar? [S] // [N]').strip().upper()[0]
    if dec == 'N':
        break
print(f'Você digitou {len(valores)} números: {valores}'
      f'\nVoce digitou {len(valor_par)} números pares: {valor_par}'
      f'\nE digitou {len(valor_impar)} números impares: {valor_impar}')