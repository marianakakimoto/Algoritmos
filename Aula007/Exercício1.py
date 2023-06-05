"""Faça um algoritmo que leia dois valores b e N
inteiros e positivos, calcule e mostre o valor
E, conforme a fórmula a seguir.
E = (b ** 1) + (b ** 2) + (b ** 3) + ... + (b ** N)
"""
b = int(input("Digite um número inteiro e positivo: "))
N = int(input("Digite um número inteiro e positivo: "))
E = 0
for i in range(1, N + 1):
    E += b ** i

print("O valor de E é:", E)
