'''
Desenvolva um programa que pergunte a distancia de uma
viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
km para viagens de até 200km e R$0,45 para viagens mais longas
'''

km_viagem = int(input('olá, qual foi a distancia percorrida da viagem?\nR: '))
if km_viagem <= 200:
    print(f'Sua viagem ficou no total de R${km_viagem * 0.50:.2f} reais')
else:
    print(f'Sua viagem ficou no total de R${km_viagem * 0.45:.2f} reais')