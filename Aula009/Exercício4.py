"""Faça um algoritmo que leia 20 palavras de no
máximo 10 caracteres, e após a leitura, realize
um processo qualquer que inverta os
caracteres de cada uma das palavras.
"""
lista= []
i = 1
for i in range(1, 21):
    lista.append(str(input(f"Digite a {i}ª palavra: ")))

for i in lista:
    print(lista[::-1])
