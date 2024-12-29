"""escreva um programa para aprovar um emprestimo
bancário para a compra de uma casa.
o programa vai perguntar o valor da casa, o salario do comprador
e em quantos anos ele vai pagar.
calcule o valor da prestação mensal, sabendo que ela não pode
exceder 30% do salario ou então o emprestimo será negado."""

# Exibe uma introdução amigável ao usuário
print("=" * 40)  # Linha decorativa para visual mais atrativo
print("Seja bem-vindo ao Banco Imaginário")  # Título do programa
print("=" * 40)  # Linha decorativa para visual mais atrativo

# Pergunta ao usuário se ele deseja simular um consórcio
dec = input("Gostaria de simular um consórcio? (s/n) ").strip().lower()

# Verifica se o usuário optou por simular
if dec == "s":
    print("Certo, vamos começar")  # Confirmação de início da simulação

    # Solicita os dados necessários para o cálculo do consórcio
    valor_casa = int(input("Qual seria o valor da casa negociada? R$ "))  # Valor total da casa
    renda_men = int(input("Qual seria a renda mensal? R$ "))  # Renda mensal do usuário
    anos_pgnd = int(input("Em quantos anos pretende pagar? "))  # Número de anos para pagamento

    # Calcula o valor da parcela mensal
    parcela_mensal = valor_casa / (anos_pgnd * 12)  # Total dividido pelo número de meses

    # Verifica se as condições para aprovação são atendidas
    # A parcela mensal deve ser menor ou igual a 30% da renda mensal
    if anos_pgnd <= 0 or parcela_mensal > renda_men * 0.3:
        print("Sinto muito, o consórcio foi negado, pois não atende aos requisitos necessários.")
    else:
        # Exibe os detalhes da aprovação, com o valor das parcelas e a duração do consórcio
        print(f"Parabéns! Seu consórcio foi aprovado.")
        print(f"Valor das parcelas: R${parcela_mensal:.2f} mensais, por {anos_pgnd * 12} meses.")

else:
    # Caso o usuário escolha não simular o consórcio, o programa finaliza
    print("Ok, até um próximo momento!")
    exit()  # Sai do programa
