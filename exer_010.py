"""faça um programa que leia a largura e a altura de uma parede
em metros, calcule a sua área e a quantidade de tinta
necessária para pinta-la. Sabendo que cada litro pinta
uma área de 2m²"""

# Solicita ao usuário a largura da parede e converte a entrada para número decimal (float)
larg = float(input("Digite a largura da parede: "))

# Solicita ao usuário a altura da parede e converte a entrada para número decimal (float)
alt = float(input("Digite a altura da parede: "))

# Calcula a área da parede multiplicando a largura pela altura
area = larg * alt

# Calcula a quantidade de tinta necessária, assumindo que 1 litro de tinta cobre 2m²
tinta = area / 2

# Exibe a área da parede e a quantidade de tinta necessária, formatando a quantidade de tinta com 2 casas decimais
print(f"para pintar uma parede com {area}m²,"
      f"\n vai ser necessário {tinta:.2f} litros de tinta")
