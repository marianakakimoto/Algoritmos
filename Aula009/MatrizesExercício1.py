"""Faça um algoritmo que leia uma matriz 2x2 e
imprima os seus elementos na ordem:
1,1 =
1,2 =
2,1 =
2,2 =
Obs: linha, coluna
"""

matriz = []
for i in range(2):
    linha = []
    for j in range(2):
        elemento = int(input("Digite o elemento {}x{} da matriz: ".format(i+1, j+1)))
        linha.append(elemento)
    matriz.append(linha)

print("1,1 =", matriz[0][0])
print("1,2 =", matriz[0][1])
print("2,1 =", matriz[1][0])
print("2,2 =", matriz[1][1])
