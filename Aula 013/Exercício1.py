"""Faça a implementação de uma função
recursiva que calcule a sequência de
Fibonacci, recebendo como parâmetro o
número de elementos da sequência.
"""
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

n = int(input("Digite o número de elementos da sequência de Fibonacci: "))

fibonacci_sequence = fibonacci(n)
print("Sequência de Fibonacci com", n, "elementos:", fibonacci_sequence)
