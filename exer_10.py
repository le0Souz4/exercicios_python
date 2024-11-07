"""faça um programa que leia a largura e a altura de uma parede
em metros, calcule a sua área e a quantidade de tinta
necessária para pinta-la. Sabendo que cada litro pinta
uma área de 2m²"""
larg = float(input("Digite a largura da parede: "))
alt = float(input("Digite a altura da parede: "))
area = larg * alt
tinta = area / 2

print(f"para pintar uma parede com {area}m²,"
      f"\n vai ser necessário {tinta:.2f} litros de tinta")