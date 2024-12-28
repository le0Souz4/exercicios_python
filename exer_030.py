'''
Desenvolva um programa que pergunte a distancia de uma
viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
km para viagens de até 200km e R$0,45 para viagens mais longas
'''

# Solicita ao usuário que informe a distância percorrida na viagem em quilômetros
km_viagem = int(input('Olá, qual foi a distância percorrida da viagem?\nR: '))

# Condição para verificar se a distância é menor ou igual a 200 km
if km_viagem <= 200:
    # Se a distância for menor ou igual a 200 km, o preço será R$ 0,50 por km
    print(f'Sua viagem ficou no total de R${km_viagem * 0.50:.2f} reais')
else:
    # Se a distância for maior que 200 km, o preço será R$ 0,45 por km
    print(f'Sua viagem ficou no total de R${km_viagem * 0.45:.2f} reais')
