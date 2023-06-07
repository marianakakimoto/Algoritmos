"""Faça um Algoritmo que simule 6000 jogadas
de um dado de 6 faces. Para simular o
resultado utilize a função randint
Ao final, mostre a frequência de sorteio de
cada uma das faces"""
from random import randint
frequencia = [0, 0, 0, 0, 0, 0]
for i in range(6000):
    lado = randint(1, 6)
    frequencia[lado - 1] += 1

for i in range(6):
    print(f"Frequência FACE {i + 1}: {frequencia[i]}")
