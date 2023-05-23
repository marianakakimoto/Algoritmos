x = str(input("Digite um número positivo: "))
soma = 0
mult = 1
for i in x:
    y = int(i)
    soma += y
    mult *= y
print(f"Multiplicação: {mult}\n"
      f"Soma: {soma}")