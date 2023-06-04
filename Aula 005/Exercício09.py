"""Dados três valores X, Y e Z, verificar se eles
podem ser os comprimentos dos lados de um
triângulo e, se forem, verificar se é um
triângulo eqüilátero, isósceles ou escaleno.
Se eles não formarem um triângulo, escrever
uma mensagem.
Considerar que:
•O comprimento de cada lado de um triângulo é menor que a soma dos outros
dois lados;
•Chama-se eqüilátero o triângulo que tem três lados iguais;
•Chama-se isósceles o triângulo que tem o comprimento de dois lados iguais;
•Chama-se escaleno o triângulo que tem os três lados diferentes"""
X = float(input("Digite o valor de X: "))
Y = float(input("Digite o valor de Y: "))
Z = float(input("Digite o valor de Z: "))
if X < Y + Z and Y < X + Z and Z < X + Y:
    if X == Y == Z:
        print("Triângulo equilátero")
    elif X == Y or X == Z or Y == Z:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Não forma um triângulo")
