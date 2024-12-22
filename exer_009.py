"""crie um programa que leia quanto dinheiro
uma pessoa tem na carteira e mostra quantos
dólares e euros ela pode comprar"""

# Define o valor do dólar em reais.
# Neste exemplo, o dólar está sendo considerado como R$5.70.
dol = 5.70

# Define o valor do euro em reais.
# Neste exemplo, o euro está sendo considerado como R$6.15.
eur = 6.15

# Solicita ao usuário que informe a quantidade de reais que ele possui.
# A função input() captura o valor como texto, e float() converte para um número decimal (permitindo casas decimais).
wal = float(input("Quantos reais você possui em mãos?: R$"))

# Calcula e exibe o saldo do usuário, além de informar quanto ele pode comprar em dólares e euros.
# A f-string é usada para formatar a mensagem, com os valores calculados diretamente no texto.
# O formato {:.2f} é usado para exibir os valores em dólares e euros com duas casas decimais.
print(f"Seu saldo atual é R${wal} "
      f"\nVocê pode comprar US${wal / dol:.2f} e €{wal / eur:.2f}")
