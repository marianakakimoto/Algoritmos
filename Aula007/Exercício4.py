"""Faça um algoritmo que:
-Leia um número indeterminado de números
que representam, cada um, a idade de um
indivíduo.
-Para finalizar, o usuário deverá digitar 0, que
não entrará nos cálculos.
- Calcule e mostre a idade média e o número
total de pessoas deste grupo de indivíduos."""
idades = []
numeroPessoas = 0
somaIdades = 0

while True:
    idade = int(input("Digite a idade (ou 0 para sair): "))

    if idade == 0:
        break

    idades.append(idade)
    numeroPessoas += 1
    somaIdades += idade

if numeroPessoas > 0:
    mediaIdades = somaIdades / numeroPessoas
    print("A idade média é:", mediaIdades)

print("O número total de pessoas é:", numeroPessoas)
