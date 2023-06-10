"""Faça um algoritmo que leia os valores de uma
matriz 3x3 de elementos reais e crie a matriz
transposta da matriz fornecida.
Matriz transposta: Igual a simétrica. Em
matemática, é o resultado da troca de linhas por
colunas em uma determinada matriz.
A[i,j] = A[j,i]
"""
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        elemento = float(input("Digite o elemento {}x{} da matriz: ".format(i+1, j+1)))
        linha.append(elemento)
    matriz.append(linha)

matriz_transposta = [[matriz[j][i] for j in range(3)] for i in range(3)]

print("Matriz Transposta:")
for linha in matriz_transposta:
    for elemento in linha:
        print(elemento, end=" ")
    print()
