"""Faça um algoritmo que receba uma matriz 10x10
de elementos inteiros e localize a posição (linha
e coluna) do maior elemento da matriz.
"""
matriz = []
for i in range(10):
    linha = []
    for j in range(10):
        elemento = int(input("Digite o elemento da matriz na posição {}x{}: ".format(i+1, j+1)))
        linha.append(elemento)
    matriz.append(linha)

maior_elemento = matriz[0][0]
linha_maior = 0
coluna_maior = 0

for i in range(10):
    for j in range(10):
        if matriz[i][j] > maior_elemento:
            maior_elemento = matriz[i][j]
            linha_maior = i
            coluna_maior = j

print("Posição do maior elemento:")
print("Linha:", linha_maior+1)
print("Coluna:", coluna_maior+1)
