"""Faça um algoritmo que calcule e mostre a
área de um círculo. Sabe-se que:
Area= π * R2
π = 3,1415"""

from math import pi, pow
raio = float(input("Digite o raio do círculo: "))
area = pi * pow(raio, 2)
print(f"Área do círculo: {area:.3f}; \n"
      f"Valor de pi: {pi:.4f}")
