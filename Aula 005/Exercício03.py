"""Faça um programa que receba um número
inteiro e verifique se esse número é par ou
ímpar"""
n = int(input("Digite um número: "))
if n % 2 == 0:
    print(f"{n} é um número par.")
else:
    print(f"{n} é um número ímpar.")
