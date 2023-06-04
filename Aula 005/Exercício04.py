"""Tendo como dados de entrada a altura e o
sexo de uma pessoa, construa um algoritmo
que calcule seu peso ideal, utilizando as
seguintes fórmulas:
- para homens: (72.7 * h) – 58;
- para mulheres: (62.1 * h) – 44.7"""

h = int(input("Digite a altura (cm): "))
sexo = (input("Digite o sexo (F ou M): "))
altura = h / 100
pesoM = 72.7 * altura - 58
pesoF = 62.1 * altura - 44.7
if sexo == "M":
    print(f"Seu peso ideal é: {pesoM:.2f}.")
else:
    if sexo == "F":
        print(f"Seu peso ideal é {pesoF:.2f}.")
