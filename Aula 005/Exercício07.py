"""Faça um programa que receba a idade de um
nadador e mostre a sua categoria usando as
regras a seguir:
Categoria Idade
Infantil 5 a 7
Juvenil 8 a 10
Adolescente 11 a 15
Adulto 16 a 30
Sênior Acima de 30"""
idade = int(input("Digite a idade do nadador: "))
if 5 > idade < 7:
    print("Categoria Infantil")
if 8 <= idade <= 10:
    print("Categoria Juvenil")
if 11 <= idade <= 15:
    print("Categoria Adolescente")
if 16 <= idade <= 30:
    print("Categoria Adulto")
if idade >= 31:
    print("Categoria Sênior")
