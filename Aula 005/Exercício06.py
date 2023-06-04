"""FAZER UM PROGRAMA QUE RECEBA DOIS
NÚMEROS E EXECUTE AS OPERAÇÕES
LISTADAS A SEGUIR DE ACORDO COM A
ESCOLHA DO USUÁRIO:
1. Média entre os números digitados
2. Diferença do maior pelo menor
3. Produto entre os números digitados
4. Divisão do primeiro pelo segundo
"""
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))
media = x + y / 2
if x >= y:
    diferenca = x - y
else:
    diferenca = y - x
produto = x * y
divisao = x / y

print(f"Média: {media}\n" 
      f"Diferença: {diferenca}\n"
      f"Produto: {produto}\n"
      f"Divisão: {divisao:.2f}\n")
