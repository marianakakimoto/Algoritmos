"""Faça um algoritmo para determinar se um
determinado vetor, digitado pelo usuário, é
um palíndromo.
Palíndromo: lido da direita para a esquerda,
ou vice versa, representam a mesma coisa.
Ex: AMA"""
palavra = str(input("Digite uma palavra: "))
inverso = palavra[::-1]
if inverso == palavra:
    print("Esta palavra é um palíndromo!")
else:
    print("Essa palavra não é um palíndromo!")
