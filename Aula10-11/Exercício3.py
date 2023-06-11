"""Faça algoritmo que carregue duas listas de dez
elementos numéricos inteiros cada um. A
partir dessas duas listas, crie um conjunto da
união entre essas duas listas."""
lista = []
lista2 = []
for i in range(10):
    lista.append(int(input("Digite um número inteiro (lista 1): ")))
    lista2.append(int(input("Digite um número inteiro (lista 2): ")))
print(set(lista).union(lista2))
