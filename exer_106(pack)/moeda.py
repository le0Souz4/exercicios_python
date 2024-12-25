# Função para aumentar um valor em uma porcentagem especificada
def aumentar(n, p=None):  
    n += n * (p / 100)  # Calcula o aumento: multiplica o valor da porcentagem (p) pelo número (n) e soma ao valor original.
    return n  # Retorna o novo valor, já aumentado.

# Função para diminuir um valor em uma porcentagem especificada
def diminuir(n, p=None):  
    n -= n * (p / 100)  # Calcula a redução: multiplica o valor da porcentagem (p) pelo número (n) e subtrai do valor original.
    return n  # Retorna o novo valor, já diminuído.

# Função para calcular o dobro de um número
def dobro(n):  
    n *= 2  # Multiplica o número (n) por 2.
    return n  # Retorna o dobro do número.

# Função para calcular a metade de um número
def metade(n):  
    n /= 2  # Divide o número (n) por 2.
    return n  # Retorna a metade do número.

# Função para formatar um número como valor monetário
def moeda(n, moeda="R$"):  
    # Formata o número com duas casas decimais, utilizando o símbolo da moeda especificada.
    # O `replace('.', ',')` converte o ponto decimal em vírgula para formato brasileiro.
    return f'{moeda}{n:,.2f}'.replace('.', ',')  
