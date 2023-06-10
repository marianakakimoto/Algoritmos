"""Crie um algoritmo que receba uma matriz 8x8
com números inteiros e mostre uma mensagem
dizendo se a matriz digitada é simétrica ou não.
Uma matriz só pode ser considerada simétrica
se A[i,j] = A[j,i]
"""
matriz = []
for i in range(8):
    linha = []
    for j in range(8):
        elemento = int(input("Digite o elemento da matriz na posição {}x{}: ".format(i+1, j+1)))
        linha.append(elemento)
    matriz.append(linha)

simetrica = True
for i in range(8):
    for j in range(i+1, 8):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
            break

if simetrica:
    print("A matriz é simétrica.")
else:
    print("A matriz não é simétrica.")
