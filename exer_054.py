"""
Faça um programa que leia o peso de 
cinco pessoas. No final, mostre qual foi o 
maior e o menor peso lidos.
"""

# Inicializamos as variáveis para armazenar o maior e o menor peso
# Usamos None inicialmente, pois queremos comparar valores reais posteriormente.
maior_peso = None
menor_peso = None

# Laço para processar os pesos de 5 pessoas
for pessoa in range(1, 6):  # O laço executará 5 vezes (uma para cada pessoa)
    peso = float(input(f"Digite o peso da {pessoa}ª pessoa (em kg): "))  # Solicitamos o peso
    
    # Na primeira iteração, definimos o peso como maior e menor automaticamente
    if maior_peso is None or menor_peso is None:  
        maior_peso = peso
        menor_peso = peso
    else:
        # Atualizamos o maior peso, se o peso atual for maior que o armazenado
        if peso > maior_peso:  
            maior_peso = peso
        # Atualizamos o menor peso, se o peso atual for menor que o armazenado
        if peso < menor_peso:  
            menor_peso = peso

# Exibimos os resultados
print(f"\nO maior peso registrado foi: {maior_peso:.2f} kg")
print(f"O menor peso registrado foi: {menor_peso:.2f} kg")

