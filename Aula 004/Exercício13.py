"""Sabe-se que o quilowatt de energia custa
um oitavo do salário mínimo. Faça um
algoritmo que receba o valor do salário
mínimo e a quantidade de quilowatts
consumida por uma residência. Calcule e
mostre:
a) O valor, em reais, de cada quilowatt
b) O valor, em reais, a ser pago por essa
residência
c) O valor, em reais, a ser pago com desconto
de 15%"""

salarioMinimo = float(input("Digite o valor do salário mínimo: "))
quilowatts = float(input("Digite a quantidade de quilowatts consumida: "))
valorKw = salarioMinimo / 80
total = valorKw * quilowatts
valorDesconto = total - (15 / 100) * total
print(f"=============================================================================\n"
      f"a) O valor, em reais, de cada quilowatt: R$ {valorKw:.2f}\n"
      f"b) O valor, em reais, a ser pago: R$ {total:.2f}\n"
      f"c) O valor, em reais, a ser pago com desconto de 15%: R$ {valorDesconto:.2f}")
