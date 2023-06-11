"""Faça uma função que determine se um ano
qualquer, no formato AAAA, é bissexto.
A função retorna 1 se o ano é bissexto e
0(zero) se não."""


def verificar_bissexto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        return 1
    else:
        return 0

# Solicitar ao usuário um ano
ano = int(input("Digite um ano (formato AAAA): "))

# Chamar a função e exibir o resultado
resultado = verificar_bissexto(ano)
print("Resultado:", resultado)
