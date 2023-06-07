"""Faça um algoritmo para determinar quantas
palavras existem em uma determinada frase
Obs: tanto a palavra, quanto a frase, devem
ser informadas pelo usuário."""

frase = str(input("Digite uma frase: "))
contador = frase.split()
print(f"Essa frase tem {len(contador)} palavras.")
