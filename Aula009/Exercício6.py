"""Faça um algoritmo que simule a jogada de dois
dados de 6 faces. O programa deve usar randint
para rolar o primeiro dado e deve usar randint
novamente para rolar o segundo dado. A soma
das duas faces deve ser calculada. Assim: a
soma variará de 2 a 12
O programa deve rolar 30.000 vezes e mostrar
a frequência com que a soma (de 2 a 12)
aparecem. Verifique se o valor 7 corresponde a
1/6 das jogadas!"""

from random import randint

frequencia = [0] * 11

for _ in range(30000):

    dado1 = randint(1, 6)

    dado2 = randint(1, 6)

    soma = dado1 + dado2

    frequencia[soma - 2] += 1

for i in range(11):
    soma = i + 2
    print(f"Frequência da soma {soma}: {frequencia[i]}")


porcentagem7 = (frequencia[5] / 30000) * 100
print(f"\nPorcentagem de vezes que a soma é 7: {porcentagem7:.2f}%")
