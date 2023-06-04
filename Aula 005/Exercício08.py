"""Faça um programa que receba o preço líquido de
um produto e o seu código de origem e mostre a sua
procedência e o preço final, calculado pelo imposto
relativo a sua procedência. A procedência obedece
a tabela a seguir:
Código Origem Procedência % Imposto
1 Sul 11%
2 Norte 13%
3 Nordeste 9%
4 Centro-Oeste 12%
5 Sudente 18%
"""
precoLiquido = float(input("Digite o preço líquido do produto: "))
codOrigem = (input("Digite o código de origem do produto: "))
if codOrigem == "1":
    imposto = precoLiquido * 11 / 100
    precoFinal = imposto + precoLiquido
    print(f"Procedência: SUL\n"
          f"Imposto: {imposto}\n"
          f"Preço final: {precoFinal}")

if codOrigem == "2":
    imposto = precoLiquido * 13 / 100
    precoFinal = imposto + precoLiquido
    print(f"Procedência: NORTE\n"
          f"Imposto: {imposto}\n"
          f"Preço final: {precoFinal}")

if codOrigem == "3":
    imposto = precoLiquido * 9 / 100
    precoFinal = imposto + precoLiquido
    print(f"Procedência: NORDESTE\n"
          f"Imposto: {imposto}\n"
          f"Preço final: {precoFinal}")

if codOrigem == "4":
    imposto = precoLiquido * 12 / 100
    precoFinal = imposto + precoLiquido
    print(f"Procedência: CENTRO-OESTE\n"
          f"Imposto: {imposto}\n"
          f"Preço final: {precoFinal}")

if codOrigem == "5":
    imposto = precoLiquido * 18 / 100
    precoFinal = imposto + precoLiquido
    print(f"Procedência: SUDESTE\n"
          f"Imposto: {imposto}\n"
          f"Preço final: {precoFinal}")
