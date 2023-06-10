"""Faça um algoritmo que leia uma matriz 2x2,
calcule e mostre uma matriz resultante que
será a matriz digitada, multiplicada pelo
maior elemento da matriz"""
matriz = []
for i in range(2):
    linha = []
    for j in range(2):
        elemento = int(input("Digite o elemento {}x{} da matriz: ".format(i+1, j+1)))
        linha.append(elemento)
    matriz.append(linha)

maior_elemento = max(max(matriz))

matriz_resultante = [[elemento * maior_elemento for elemento in linha] for linha in matriz]

print("Matriz Resultante:")
for linha in matriz_resultante:
    for elemento in linha:
        print(elemento, end=" ")
    print()
