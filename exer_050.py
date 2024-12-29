"""
Desenvolva um programa que leia o primeiro termo 
e a razão de uma PA. No final, mostre os 10 primeiros 
termos dessa progressão.
"""

# Solicita ao usuário o primeiro termo da PA e sua razão.
primeiro_termo = int(input("Digite o primeiro termo da PA: "))  # Primeiro termo da progressão.
razao = int(input("Digite a razão da PA: "))  # Diferença constante entre os termos.

# Exibe uma mensagem inicial para indicar o início da progressão.
print("Os 10 primeiros termos da PA são:")

# Laço para calcular e exibir os 10 primeiros termos da PA.
for n in range(10):  # O laço executa 10 vezes, pois queremos mostrar 10 termos.
    termo_atual = primeiro_termo + n * razao  # Fórmula geral da PA: termo = primeiro_termo + (n * razão).
    print(termo_atual, end=" → ")  # Exibe o termo atual, com um separador visual.

print("Fim")  # Indica o término da exibição.
