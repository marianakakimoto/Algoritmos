"""Cada degrau de uma escada tem Xcm de
altura. Faça um algoritmo que receba a
altura de cada degrau em cm e a altura que
o usuário deseja alcançar subindo a escada
(em metros). Faça as conversões, calcule e
mostre quantos degraus o usuário deverá
subir para atingir seu objetivo.
Obs: não se preocupe com a altura do
usuário!"""

alturaDegrau = int(input("Informe a altura de cada degrau (em cm): "))
altura = int(input("Informe a altura que você deseja alcançar (em metros) com a escada: "))
degraus = int((altura * 100) / alturaDegrau)
print(f"===================================================================\n"
      f"De acordo com as informações, sua escada terá {degraus} degraus!")
