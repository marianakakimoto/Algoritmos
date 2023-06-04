"""Faça um algoritmo que leia o ano de
nascimento de uma pessoa, calcule e
mostre sua idade e, também, verifique e
mostre se ela já tem idade para votar (16
anos ou mais) e para conseguir a Carteira
de Habilitação (18 anos ou mais)"""
anoNasc = int(input("Digite o seu ano de nascimento: "))
anoAtual = int(input("Digite o ano atual: "))
idade = anoAtual - anoNasc
if idade >= 16:
    print("Você tem idade suficiente para votar.")
else:
    print("Você não tem idade suficiente para votar.")
if idade >= 18:
    print("Você já tem idade para conseguir Carteira de Habilitação")
else:
    print("Você não tem idade para conseguir Carteira de Habilitação")
