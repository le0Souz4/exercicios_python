"""
Escreva um programa que pergunte a quantidade de Km 
percorridos por um carro alugado e a quantidade de dias 
pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

# Solicita ao usuário o número de dias que o carro foi alugado e calcula o valor correspondente.
# Multiplicamos o número de dias por 60, pois cada dia custa 60 reais.
dias = int(input('Por quantos dias o carro foi alugado?: ')) * 60

# Solicita ao usuário o número de quilômetros rodados e calcula o valor correspondente.
# Multiplicamos os quilômetros rodados por 0.15, pois cada quilômetro rodado custa 0.15 reais.
km_rodado = float(input('Agora informe quantos kms foram rodados: ')) * 0.15

# Calcula o total a ser pago, somando o valor dos dias alugados e o valor dos quilômetros rodados.
total = dias + km_rodado

# Exibe o valor dos dias alugados e o valor dos quilômetros rodados.
print(f'Ok, o total de dias alugados ficou em {dias} reais '
      f'\no total de kms rodados ficou em {km_rodado} reais')

# Exibe o valor total a ser pago.
print(f'Sua conta ficou no total de {total} reais')
