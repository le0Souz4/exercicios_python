"""
Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses. Seu aplicativo deverá analisar se a expressão
passada está com os parênteses abertos e fechados na ordem correta.
"""

# Solicita ao usuário a entrada da expressão
expressao = input("Digite uma expressão com parênteses: ")

# Lista para controlar os parênteses
pilha = []

# Percorre cada caractere da expressão
for char in expressao:
    if char == '(':
        # Adiciona parêntese aberto à lista
        pilha.append(char)
    elif char == ')':
        # Verifica se há parênteses abertos na lista
        if '(' in pilha:
            # Remove o parêntese correspondente da lista
            pilha.remove('(')
        else:
            # Não há correspondência para este parêntese fechado
            pilha.append(')')
            break

# Verifica se a lista está vazia
if not pilha:
    print("A expressão está correta!")
else:
    print("A expressão está incorreta!")
