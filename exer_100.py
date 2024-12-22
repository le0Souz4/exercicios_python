"""
Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento
de uma pessoa, retornando um valor literal indicando
se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""

def voto(idade):
    if idade < 16:
        return "negado"
    elif (16 <= idade >18) and (idade > 65) :
        return "opcional"
    elif idade >= 18:
        return "obrigatório"

# programa principal
resp1 = int(input('idade: '))
print(f'Por sua idade ser {resp1}, seu voto é {voto(resp1)}')