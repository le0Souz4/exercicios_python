"""
Escreva um programa que pergunte a quantidade de Km 
percorridos por um carro alugado e a quantidade de dias 
pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

dias = int(input('por quantos dias o carro foi alugado?: ')) * 60
km_rodado = float(input('agora informe quantos kms foram rodados: ')) * 0.15
total = dias + km_rodado
print(f'ok, o total de dias alugados ficou em {dias} reais \no total de kms rodados ficou em {km_rodado} reais')
print(f'sua conta ficou no total de {total} reais')
