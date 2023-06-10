"""Faça um algoritmo que leia os dados de uma
matriz de 4 linhas e 4 colunas, composta de
elementos reais, e calcule a soma dos
elementos da diagonal principal da matriz.
"""
matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        elemento = float(input("Digite o elemento {}x{} da matriz: ".format(i+1, j+1)))
        linha.append(elemento)
    matriz.append(linha)

soma_diagonal = 0
for i in range(4):
    soma_diagonal += matriz[i][i]

print("A soma dos elementos da diagonal principal é:", soma_diagonal)
