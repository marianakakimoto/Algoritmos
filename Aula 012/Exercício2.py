"""Faça uma função que retorne o valor lógico V
(verdadeiro) se o número inteiro passado por
parâmetro for primo, e F (falso) se não.
Implemente sua função em um programa
completo."""


def verificar_primo(numero):
    if numero < 2:
        return "F"
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return "F"
    return "V"
numero = int(input("Digite um número inteiro: "))
resultado = verificar_primo(numero)
print("Resultado:", resultado)
