"""Faça um algoritmo para ler nove caracteres
numéricos em uma string. Mostre o conteúdo
dessa string colando pontos e virgula,
respectivamente nas posições inteiras e
decimais.
Exemplo:
Digitado> 987654321
Mostrado> 9.876.543,21
"""
n = str(input("Digite 9 caracteres numéricos: "))
decimais = n[7:9]
centenas = n[4:7]
milhares = n[1:4]
bi = n[0]

print(f"{bi}.{milhares}.{centenas},{decimais}")
