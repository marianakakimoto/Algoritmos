"""Faça um algorimto que carregue um
dicionário de 10 elementos onde a chave é o
sobrenome da pessoa e o valor a sua idade.
Após a finalização da entrada, o algoritmo
deve escrever o sobrenome da pessoa com
maior idade.
"""
dic = {}

for i in range(10):
    sobrenome = (input("Digite o nome: "))
    idade = int(input("Digite a idade: "))
    dic[sobrenome] = idade
maior_idade = max(dic.values())
sobrenome_mais_idade = [sobrenome for sobrenome, idade in dic.items() if idade == maior_idade][0]
print("O sobrenome da pessoa com maior idade é:", sobrenome_mais_idade)
