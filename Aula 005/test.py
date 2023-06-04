x = float(input("Lado 1: "))
y = float(input("Lado 2: "))
z = float(input("Lado 3: "))
if x or y or z < x + y or x + z or y + z:
    print("Não é um triângulo.")
else:
    if x == y == z:
        print("É um triângulo equilátero.")
    if x == y or x == z or y == z:
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")