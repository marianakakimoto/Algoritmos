"""Faça um algoritmo que receba uma matriz de
5x5 com números reais. Ao final o algoritmo
deve calcular e mostrar a média dos elementos
que estão nas linhas pares da matriz"""
matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        elemento = float(input("Digite o elemento da matriz na posição {}x{}: ".format(i+1, j+1)))
        linha.append(elemento)
    matriz.append(linha)

soma = 0
contador = 0
for i in range(1, 5, 2):
    for j in range(5):
        soma += matriz[i][j]
        contador += 1

media = soma / contador

print("A média dos elementos das linhas pares da matriz é:", media)
