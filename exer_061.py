"""Melhore o DESAFIO 61, perguntando para o usuário 
se ele quer mostrar mais alguns termos. O programa 
encerrará quando ele disser que quer mostrar 0 termos."""

# Solicita o primeiro termo e a razão da PA ao usuário
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

# Inicializa as variáveis
termo = primeiro_termo  # Valor atual do termo
contador = 1  # Contador de termos exibidos
total_termos = 0  # Total de termos exibidos
mais_termos = 10  # Quantidade inicial de termos a serem mostrados

# Laço principal
while mais_termos != 0:  # Continua enquanto o usuário não escolher 0 termos adicionais
    total_termos += mais_termos  # Atualiza o total de termos a serem exibidos
    while contador <= total_termos:  # Gera e exibe os termos da PA
        print(f"{termo}", end=" -> ")
        termo += razao  # Calcula o próximo termo
        contador += 1  # Incrementa o contador
    print("PAUSA")  # Indica que a exibição atual terminou
    # Pergunta ao usuário quantos termos adicionais ele deseja
    mais_termos = int(input("Quantos termos você quer mostrar a mais? "))

print(f"Progressão finalizada com {total_termos} termos exibidos.")  # Mensagem final
