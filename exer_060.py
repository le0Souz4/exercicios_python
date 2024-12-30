"""Refaça o DESAFIO 50, lendo o primeiro termo
e a razão de uma PA, mostrando os 10 primeiros 
termos da progressão usando a estrutura while."""

# Solicita ao usuário o primeiro termo e a razão da PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

# Inicializa as variáveis
termo = primeiro_termo  # Armazena o valor atual do termo, começando pelo primeiro
contador = 1  # Contador para rastrear o número de termos exibidos

# Estrutura while para gerar e exibir os 10 primeiros termos da PA
while contador <= 10:  # A condição garante que serão exibidos exatamente 10 termos
    print(f"{termo}", end=" -> ")  # Exibe o termo atual e seta a formatação com "->"
    termo += razao  # Atualiza o valor do termo, adicionando a razão
    contador += 1  # Incrementa o contador para rastrear os termos exibidos

print("FIM")  # Indica o fim da progressão
