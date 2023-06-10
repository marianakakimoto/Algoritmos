"""Faça um algoritmo que leia uma matriz 10x20
com números inteiros e some cada uma das
linhas, armazenando o resultado das somas em
um vetor. A seguir, multiplique cada elemento
da matriz pela soma da linha e mostre a matriz
resultante"""
matriz = []
for i in range(10):
    linha = []
    for j in range(20):
        elemento = int(input("Digite o elemento da matriz na posição {}x{}: ".format(i+1, j+1)))
        linha.append(elemento)
    matriz.append(linha)

somas_linhas = []
for linha in matriz:
    soma = sum(linha)
    somas_linhas.append(soma)

matriz_resultante = []
for i in range(10):
    linha_resultante = []
    for j in range(20):
        elemento_resultante = matriz[i][j] * somas_linhas[i]
        linha_resultante.append(elemento_resultante)
    matriz_resultante.append(linha_resultante)

print("Matriz Resultante:")
for linha in matriz_resultante:
    for elemento in linha:
        print(elemento, end=" ")
    print()
