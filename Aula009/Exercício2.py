"""Faça um algoritmo que carregue um vetor de
10 elementos numéricos inteiros.
Após a finalização da entrada, o algoritmo
deve escrever o maior valor e sua posição.
"""
lista = []
for i in range(0, 9):
    lista.append(input("Digite um número inteiro: "))

print(f'Valor máximo: {max(lista)}\n'
      f'Posição: {lista.index(max(lista))}')
