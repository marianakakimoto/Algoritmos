"""Faça um algoritmo que receba o ano de
nascimento de uma pessoa e o ano atual
e mostre:
a) A idade dessa pessoa em anos;
b) A idade dessa pessoa em meses;
c) A idade dessa pessoa em semanas;
d) A idade dessa pessoa em dias."""

anoNasc = int(input("Digite o seu ano de nascimento: "))
anoAtual = int(input("Digite o ano atual: "))

idadeAno = anoAtual - anoNasc
idadeMeses = idadeAno * 12
idadeSemanas = idadeAno * 52
idadeDias = idadeSemanas * 7

print(f"Você tem {idadeAno} anos, "
      f"aproximadamente {idadeMeses} meses, "
      f"{idadeSemanas} semanas e "
      f"{idadeDias} dias.")
