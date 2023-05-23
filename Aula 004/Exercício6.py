"""Faça um algoritmo que receba o salário de
um funcionário e o percentual de aumento,
calcule e mostre o valor do aumento e o
novo salário."""

salario = float(input("Digite o salário: "))
aumento = float(input("Digite o percentual de aumento (sem %, ex.: 15): "))
novoSalario = salario + ((aumento/100) * salario)
print(f"Salário atual: R$ {salario}; \n"
      f"Aumento: {aumento}%; \n"
      f"Novo salário: R$ {novoSalario}.")
