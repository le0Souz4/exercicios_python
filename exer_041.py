"""
 Refaça o DESAFIO 34 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
"""

# Solicitar os lados do triângulo
lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

# Verificar se as retas podem formar um triângulo
if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
    print("As retas podem formar um triângulo!", end=" ")
    
    # Verificar o tipo de triângulo
    if lado1 == lado2 == lado3:
        print("E o tipo é: EQUILÁTERO (todos os lados iguais)")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("E o tipo é: ISÓSCELES (dois lados iguais, um diferente)")
    else:
        print("E o tipo é: ESCALENO (todos os lados diferentes)")
else:
    print("As retas NÃO podem formar um triângulo!")
