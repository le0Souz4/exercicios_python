"""escreva um programa que leia um valor em metros
e o exiba convertido em centimetros e milimetros"""

# Solicita ao usuário que insira uma distância em metros.
# A função input() captura o valor como texto, e float() converte para número decimal (com casas decimais, se necessário).
met = float(input("Digite o valor em metros: "))

# Converte o valor de metros para centímetros.
# Multiplica o valor em metros por 100, já que 1 metro equivale a 100 centímetros.
cen = met * 100

# Converte o valor de metros para milímetros.
# Multiplica o valor em centímetros por 10 ou o valor em metros diretamente por 1000.
mil = cen * 10

# Exibe os valores convertidos.
# A f-string permite exibir os valores formatados diretamente no texto.
print(f"{met} metros em centímetros vale {cen} e em milímetros vale {mil}")
