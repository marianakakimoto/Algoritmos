"""Faça um algoritmo que lê 10 números inteiros e
os armazena em um vetor A.
Depois de armazenado, o algoritmo fará a
ordenação desses números (em ordem
crescente de valores) e os colocará no vetor B
Ao final o algoritmo deve mostrar os dois
vetores: A e B"""
A = []
B = []
for i in range(1, 11):
    A.append(int(input(f"Digite o {i}º número: ")))

B = sorted(A)

print("Lista não ordenada - A: ", A)
print("Lista em ordem crescente - B: ", B)
