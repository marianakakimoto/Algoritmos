def primo(n):
    i = 1
    contador = 0
    while i <= n:
        if (n % i) == 0:
            contador += 1
        i += 1
    if contador == 2:
        return True
    else:
        return False


def qtdprimo(x):
    lista = []
    for i in range(0, x+1):
        if primo(i):
            print(i, end=' - ')
            lista.append(i)
            print(lista)
            return print("Valor da soma de todos os números: ", sum(lista))


qtdprimo(9)
