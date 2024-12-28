"""
Escreva um programa que leia a velocidade de um carro,
se ele ultrapassar 80km/h, mostre uma mensagem dizendo que
ele foi multado. A multa vai custar R$7,00 por cada acima
do limite.
"""

# Solicita ao usuário que informe a velocidade do veículo
km_hora = int(input('O veículo estava a qual velocidade? '))

# Calcula o valor da multa caso a velocidade seja superior a 80 km/h
multa = (km_hora - 80) * 7

# Verifica se a velocidade é maior que 80 km/h
if km_hora > 80:
    # Se a velocidade for acima de 80 km/h, imprime a mensagem de infração e o valor da multa
    print('Velocidade acima da tolerada'
          f'\nUma multa de R${multa:.2f} será cobrada')
else:
    # Caso a velocidade esteja dentro do limite permitido, imprime a mensagem de conformidade
    print('Velocidade dentro da permitida')
