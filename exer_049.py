"""desenvolva um programa que leia seis numeros
inteiros e mostre a soma apenas daqueles que forem
pares, se o valor digitado for impar, desconsidere-o"""

# Inicializamos duas variáveis para armazenar as somas de números pares e ímpares separadamente.
soma_par = 0  # Variável que acumulará a soma dos números pares.
soma_imp = 0  # Variável que acumulará a soma dos números ímpares.

# Criamos um laço 'for' para repetir o processo de entrada de números exatamente 6 vezes.
for count in range(1, 7):  # O 'range(1, 7)' gera os números de 1 a 6, representando a contagem de entradas.
    numero = int(input(f"Digite o {count}° numero: "))  # Solicita que o usuário insira um número inteiro.
    
    # Verificamos se o número é par ou ímpar usando o operador de módulo (%).
    if numero % 2 == 0:  # Se o resto da divisão do número por 2 for 0, significa que é par.
        soma_par += numero  # Adicionamos o número à variável 'soma_par'.
    elif numero % 2 != 0:  # Caso contrário, se o resto não for 0, o número é ímpar.
        soma_imp += numero  # Adicionamos o número à variável 'soma_imp'.

# Após o término do laço (quando os 6 números forem inseridos), exibimos os resultados.
print("A soma de todos os numeros PARES é:", soma_par)  # Exibe a soma acumulada dos números pares.
print("A soma de todos os numeros IMPARES é:", soma_imp)  # Exibe a soma acumulada dos números ímpares.
