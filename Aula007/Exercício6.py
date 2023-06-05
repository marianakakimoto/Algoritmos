"""Faça um programa que receba um número inteiro x.
Calcule e mostre o fatorial desse número (x!)"""
x = int(input("Digite um número inteiro: "))
fatorial = 1

if x < 0:
    print("Erro: O fatorial é indefinido para números negativos.")
elif x == 0:
    print("O fatorial de 0 é 1.")
else:
    for i in range(1, x + 1):
        fatorial *= i

    print("O fatorial de", x, "é", fatorial)
