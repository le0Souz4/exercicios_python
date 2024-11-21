"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente 
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
"""

cat_opo = float(input('digite o comprimento do cateto oposto: '))
cat_adj = float(input('agora digite o comprimento do cateto adjacente: '))
hipo = cat_opo**2 + cat_adj**2
print(f'por meio do teorema de pitágoras, o comprimento da hipotenusa será de {hipo**(1/2):.2f}')
