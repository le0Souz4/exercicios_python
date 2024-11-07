"""escreva um programa que leia um valor em metros
e o exiba convertido em centimetros e milimetros"""

met = float(input("Digite o valor em metros: "))
cen = met * 100
mil = cen * 100
print(f"{met} em centimetros vale {cen} e em milimetros vale {mil}")