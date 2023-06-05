"""Faça um programa que receba um número inteiro maior
que 1. Ele deve verificar se o número fornecido é primo
ou não, e mostrar a mensagem correspondente.
Lembre-se: um número primo só é divisível por 1 ou por
ele mesmo"""
num = int(input("Digite um número inteiro maior que 1: "))

primo = True

if num <= 1:
    primo = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            primo = False
            break

if primo:
    print(num, "é um número primo.")
else:
    print(num, "não é um número primo.")
