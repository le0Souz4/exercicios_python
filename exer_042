"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, 
de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
"""

# Solicitar o peso e altura da pessoa
peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))

# Calcular o IMC
imc = peso / (altura ** 2)

# Exibir o IMC e o status
print(f"O seu IMC é {imc:.2f}")

if imc < 18.5:
    print("Status: Abaixo do Peso")
elif 18.5 <= imc < 25:
    print("Status: Peso Ideal")
elif 25 <= imc < 30:
    print("Status: Sobrepeso")
elif 30 <= imc < 40:
    print("Status: Obesidade")
else:
    print("Status: Obesidade Mórbida")
