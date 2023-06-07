"""Faça um algoritmo que carregue um vetor de
10 elementos numéricos inteiros.
Após a finalização da entrada, o algoritmo
deve escrever o mesmo vetor, na ordem
inversa de entrada.
"""
vetor = []
for i in range(0, 9):
    vetor.append(input("Digite um número inteiro: "))

print(vetor[::-1])
