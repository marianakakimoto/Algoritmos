"""Faça um algoritmo que leia um número não
determinado de pares de valores [m,n], todos
inteiros e positivos, um par de cada vez e que
calcule e mostre a soma de todos os
números inteiros entre m e n (inclusive).
Na digitação dos pares m,n deve-se validar
que m é maior que n"""
somaTotal = 0

while True:
    m = int(input("Digite o valor de m: "))
    n = int(input("Digite o valor de n: "))

    if m <= n:
        print("Erro: m deve ser maior que n. Tente novamente.")
        continue

    soma = 0
    for num in range(n, m + 1):
        soma += num

    somaTotal += soma

    opcao = input("Deseja digitar mais um par de valores? (S/N): ")
    if opcao.upper() != "S":
        break

print("A soma total dos números entre m e n é:", somaTotal)
