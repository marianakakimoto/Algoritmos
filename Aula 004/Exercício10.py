"""Faça um algoritmo que receba um número
positivo e maior que zero, calcule e mostre:
a) O número digitado ao quadrado
b) O número digitado ao cubo
c) A raiz quadrada do número digitado
Observação:
Exp(x,y) – Calcula a potência de x elevado a y
Raizq(x) – Calcula a raiz quadrada de x"""

import math

x = int(input("Digite um número inteiro positivo e maior que zero: "))
xQuadrado = pow(x, 2)
xCubo = pow(x, 3)
xRaiz = math.sqrt(x)
print(f"Número ao quadrado: {xQuadrado}\n"
      f"Número ao cubo: {xCubo}\n"
      f"Raiz do número: {xRaiz}")
