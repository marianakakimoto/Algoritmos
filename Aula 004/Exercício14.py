"""Faça um algoritmo que receba uma hora
formada por hora e minutos (um número
real), calcule e mostre a hora digitada
apenas em minutos. Lembre-se de que:
◼ Para quatro e meia deve-se digitar: 4,30
◼ Os minutos vão de 0 a 60!!"""

horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
horaMin = horas * 60 + minutos
print(f"Horas em minutos: {horaMin}")
