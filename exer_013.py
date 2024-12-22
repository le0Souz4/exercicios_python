"""escreva um programa que converta uma temperatura
de celcius para fahrenheit"""

# Solicita ao usuário a temperatura em Celsius e converte a entrada para número decimal (float)
cel = float(input("Digite uma temperatura em Celsius: "))

# Converte a temperatura de Celsius para Fahrenheit utilizando a fórmula:
# (Celsius * 9/5) + 32 = Fahrenheit
fah = (cel * (9/5)) + 32

# Exibe a temperatura convertida para Fahrenheit
print(f"A temperatura em Fahrenheit será de: {fah}")
