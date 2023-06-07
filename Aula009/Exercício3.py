"""Faça algoritmo que carregue dois vetores de
dez elementos numéricos cada um e mostre
um vetor resultante na intercalação desses
dois vetores
"""
lista = []
lista2 = []
for i in range(10):
    x = str(input("Digite um número: "))
    lista.append(x)

for i in range(10):
    y = str(input("Digite um número: "))
    lista2.append(y)

lista3 = []
for i in range(10):
    lista3.append(lista[i])
    lista3.append(lista2[i])

print("Vetor resultante:")
print(lista3)
