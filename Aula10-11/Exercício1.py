"""Faça um algoritmo que carregue uma tupla
de 10 elementos numéricos inteiros.
Após a finalização da entrada, o algoritmo
deve escrever a mesma tupla, na ordem
inversa de entrada"""
tupla = ()
for i in range(10):
    elemento = tuple(input("Digite um número inteiro: "))
    tupla += elemento
tupla_invertida = tuple(reversed(tupla))
print(tupla_invertida)
