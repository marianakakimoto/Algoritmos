"""Faça um algoritmo que receba o salário de
um funcionário, calcule e mostre o novo
salário, sabendo-se que este sofreu um
aumento de 25%."""

salario = float(input("Digite o salário: "))
reajuste = (salario * 0.25)
novoSalario = reajuste + salario

print(f"Salário: R$ {salario:.2f}.\n"
      f"Novo salário: R$ {novoSalario:.2f}.")
