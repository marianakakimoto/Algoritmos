"""Faça um algoritmo que receba três notas de um aluno,
calcule e mostre a média aritmética e a mensagem que
segue a tabela abaixo. Para alunos de exame, calcule e
mostre a nota que deverá ser tirada no exame para
aprovação, considerando que a média do exame é 6,0 (e
que a média após o exame é resultado da média
aritmética entre a nota do exame e a média antes do
exame)."""

p1 = float(input("Nota Prova1: "))
p2 = float(input("Nota Prova2: "))
p3 = float(input("Nota Prova3: "))
media = (p1 + p2 + p3) / 3
if media >= 7:
    print("Aprovado!")
else:
    if media < 3:
        print("Reprovado!")
    else:
        print("Exame!")
        nota = 12 - media
        print(f"Você tem que tirar no mínimo {nota:.1f}")