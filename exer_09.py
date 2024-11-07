"""crie um programa que leia quanto dinheiro
uma pessoa tem na carteira e mostra quantos
dólares e euros ela pode comprar"""
dol = 5.70
eur = 6.15
wal = float(input("quantos reais voce possue em mãos?: R$"))
print(f"Seu saldo atual é {wal} "
       f"\nvoce pode comprar US$${wal/dol:.2f} e €{wal/eur:.2f} ")