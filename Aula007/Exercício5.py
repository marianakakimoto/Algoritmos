"""Faça um algoritmo que leia o valor do peso e da
altura de 20 pessoas. Ao final, o algoritmo deve
mostrar:
- O peso médio
- A altura média
- O maior e o menor IMC
Obs: IMC (Índice de Massa Corporal) – calculado a
partir da fórmula:"""
numPessoas = 20
pesos = []
alturas = []

for i in range(numPessoas):
    peso = float(input("Digite o peso da pessoa {}: ".format(i + 1)))
    altura = float(input("Digite a altura da pessoa {}: ".format(i + 1)))
    pesos.append(peso)
    alturas.append(altura)

somaPesos = sum(pesos)
somaAlturas = sum(alturas)
pesoMedio = somaPesos / numPessoas
alturaMedia = somaAlturas / numPessoas

imcs = []
for i in range(numPessoas):
    imc = pesos[i] / (alturas[i] ** 2)
    imcs.append(imc)

maiorImc = max(imcs)
menorImc = min(imcs)

print("O peso médio é:", pesoMedio)
print("A altura média é:", alturaMedia)
print("O maior IMC é:", maiorImc)
print("O menor IMC é:", menorImc)
