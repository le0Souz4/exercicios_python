"""
Escreva um programa que leia a velocidade de um carro,
se ele ultrapassar 80km/h, mostre uma mensagem dizendo que
ele foi multado. A multa vai custar R$7,00 por cada acima
do limite.
"""

km_hora = int(input('O veículo estava a qual velocidade? '))
multa = (km_hora - 80) * 7
if km_hora > 80:
    print('Velocidade acima da tolerada'
          f'\nUma multa de R${multa:.2f} será cobrada')
else:
    print('velocidade dentro da permitida')

