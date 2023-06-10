"""Faça um algoritmo que armazenará os 10
primeiros números primos acima de 100. Ao
final, o algoritmo deve mostrar os valores
desse vetor"""
count = 0
num = 101
primos = []

while count < 10:
    ePrimo = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            ePrimo = False
            break

    if ePrimo:
        primos.append(num)
        count += 1

    num += 1

print(primos)
