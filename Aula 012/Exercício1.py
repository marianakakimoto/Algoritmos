"""Faça uma função que retorne o valor lógico V
(verdadeiro) se o número inteiro passado por
parâmetro for par, e F (falso) se não.
Implemente sua função em um programa
completo.
"""


def verificar_par(numero):
    if numero % 2 == 0:
        return "V"
    else:
        return "F"
numero = int(input("Digite um número inteiro: "))
resultado = verificar_par(numero)
print("Resultado:", resultado)
