def cercado(totalcabecas, totalpes):
    patos = ((2 * totalcabecas - totalpes) / 2) * -1
    coelhos = (totalcabecas + totalpes) / 2
    totalpes = 2 * patos + 4 * coelhos
    totalcabecas = patos + coelhos
    return print(f"Total de patos: {patos}\n"
                 f"Total de coelhos: {coelhos}")


cercado(2, 7)
