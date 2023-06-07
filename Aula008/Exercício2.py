"""Faça um algoritmo que solicite uma data no
formato de uma string – dd/mm/aaaa. Mostre
essa data no formato AAAAMMDD"""
data_input = input("Digite uma data no formato dd/mm/aaaa: ")

if len(data_input) != 10 or data_input[2] != '/' or data_input[5] != '/':
    print("Formato de data inválido.")
else:

    dia = data_input[0:2]
    mes = data_input[3:5]
    ano = data_input[6:]

    data_formatada = ano + mes + dia

    print("Data formatada: ", data_formatada)
