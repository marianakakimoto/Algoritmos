"""Faça um programa que calcule os 10 primeiros números
da sequencia de Fibonacci"""
n = 10

fibonacci = [0, 1]

for i in range(2, n):
    termo = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(termo)

print("Os 10 primeiros números da sequência de Fibonacci são:")
for num in fibonacci:
    print(num)
