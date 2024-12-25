def aumentar(n, p = None):
    n += n * (p/100)
    return n

def diminuir(n, p = None):
    n -= n * (p/100)
    return n

def dobro(n):
    n *= 2
    return n

def metade(n):
    n /= 2
    return n