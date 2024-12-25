"""
Crie um módulo chamado moeda.py que tenha as
funções incorporadas aumentar(), diminuir(), dobro() e
metade(). Faça também um programa que importe esse módulo
e use algumas dessas funções.
"""
import moeda  # Importa um módulo personalizado chamado "moeda", onde estão definidas funções para manipulação de valores monetários.

# Entrada de um número pelo usuário, convertendo para tipo float.
numero = float(input('digite um número: '))

# Pergunta ao usuário se ele deseja calcular uma porcentagem. O valor é transformado em maiúsculo e apenas o primeiro caractere é considerado.
dec = input('deseja calcular porcentagem? ').strip().upper()[0]

# Caso o usuário tenha respondido 'S', solicita a porcentagem a ser calculada.
if dec == 'S':
    porcentagem = int(input('digite a porcentagem: '))

# Utiliza as funções definidas no módulo "moeda" para realizar cálculos:
resp1 = moeda.aumentar(numero, porcentagem)  # Calcula o aumento do número pela porcentagem.
resp2 = moeda.diminuir(numero, porcentagem)  # Calcula a diminuição do número pela porcentagem.
resp3 = moeda.dobro(numero)  # Calcula o dobro do número.
resp4 = moeda.metade(numero)  # Calcula a metade do número.

# Exibe os resultados formatados:
# As funções chamadas "moeda()" são usadas para formatar os valores no estilo monetário (ex.: "R$ 100,00").
print(f"aumentando em {porcentagem}%, fica: {moeda.moeda(resp1)}\n"  # Mostra o valor com aumento.
      f"diminuindo em {porcentagem}% fica: {moeda.moeda(resp2)}\n"  # Mostra o valor com redução.
      f"dobrando fica {moeda.moeda(resp3)}, e\n"  # Mostra o valor dobrado.
      f"diminuindo pela metade fica: {moeda.moeda(resp4)}")  # Mostra o valor reduzido à metade.

"""
!!! Este exercicio está sendo feito concomitantemente com o exer_107:
Adapte o código do desafio #106, criando uma função
adicional chamada moeda() que consiga mostrar os números
como um valor monetário formatado.
"""