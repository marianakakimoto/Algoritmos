"""Elabore um algoritmo para determinar
quantas vogais existem dentro de uma
determinada frase (que deve ser recebida do
usuário).
"""
frase = str(input("Digite uma frase: "))
contador = frase.lower()
result = {}
vogais = 'aeiouáéíóúàãõâô'
for i in vogais:
    result[i] = contador.count(i)

print(result)
