"""Faça um algoritmo que calcule a área de um triângulo.
Este algoritmo não pode permitir a entrada de dados
inválidos, ou seja, medidas menores ou iguais a zero"""
b = int(input("Digite a base do triângulo: "))
while b <= 0:
    print("Você digitou um valor inválido.")
    b = int(input("Digite a base do triângulo: "))
h = int(input("Digite a altura do triângulo: "))
while h <= 0:
    print("Você digitou um valor inválido.")
    h = int(input("Digite a altura do triângulo: "))
a = b * h / 2
print("A área do triângulo é: ", a)
