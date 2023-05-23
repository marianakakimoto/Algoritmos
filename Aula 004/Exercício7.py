"""Faça um algoritmo que receba o valor de
um depósito e o valor da taxa de juros,
calcule e mostre o valor do rendimento e
o valor total depois do rendimento."""

deposito = float(input("Valor a ser depositado: "))
taxaJuros = float(input("Taxa de juros (a.m.): "))
tempo = int(input("Tempo de aplicação (meses): "))
rendimento = deposito * (taxaJuros/100) * tempo
valorTotal = deposito + rendimento
print(f"=================================================\n"
      f"Rendimento: R$ {rendimento:.2f};\n"
      f"Valor depositado: R$ {deposito:.2f};\n"
      f"Valor total após rendimento: R$ {valorTotal:.2f}.\n"
      f"=================================================")
