"""
Faça um programa que mostre a tabuada de vários
números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo
"""

# Inicializa a variável num_1 com 0, mas ela será redefinida dentro do loop
num_1 = 0

# Inicia o loop infinito, onde o programa vai continuar até o número ser positivo
while True:
    # Solicita ao usuário que digite um número
    num_1 = int(input("Digite o número a ser multiplicado: "))
    
    # Verifica se o número digitado é negativo
    if num_1 < 0:
        print("Por favor, digite um número positivo")
    else:
        # Se o número for positivo, quebra o loop
        break

# Aqui usamos list comprehension para gerar os resultados da tabuada
# range(1, 11) cria um intervalo de 1 até 10 (11 não incluso)
# Para cada valor de i de 1 a 10, multiplicamos num_1 por i e formatamos a string
resultados = [f"{num_1} x {i} = {num_1 * i}" for i in range(1, 11)]

# O método join concatena todas as strings da lista resultados em uma única string
# usando uma quebra de linha (\n) para separar cada linha da tabuada
print("\n" + "\n".join(resultados))

# A versão alternativa sem o uso de list comprehension seria mais longa e menos eficiente:
'''print(f"\n{num_1} x 1 = {num_1 * 1}"
      f"\n{num_1} x 2 = {num_1 * 2}"
      f"\n{num_1} x 3 = {num_1 * 3}"
      f"\n{num_1} x 4 = {num_1 * 4}"
      f"\n{num_1} x 5 = {num_1 * 5}"
      f"\n{num_1} x 6 = {num_1 * 6}"
      f"\n{num_1} x 7 = {num_1 * 7}"
      f"\n{num_1} x 8 = {num_1 * 8}"
      f'\n{num_1} x 9 = {num_1 * 9}'
      f'\n{num_1} x 10 = {num_1 * 10}')'''

# Aqui está um código alternativo mais simplificado com o uso de list comprehension,
# que é mais eficiente, enxuto e visualmente mais organizado.
