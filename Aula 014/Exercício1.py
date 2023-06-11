def converter_bytes_para_mb(bytes):
    return bytes / (1024 * 1024)


def calcular_percentual(bytes, total):
    return (bytes / total) * 100

with open('usuarios.txt', 'r', encoding="UTF-8") as arquivo:
    linhas = arquivo.readlines()

espacos_utilizados = []

for linha in linhas:
    dados = linha.split()
    usuario = dados[0]
    espaco = int(dados[1])
    espacos_utilizados.append(espaco)

espaco_total = sum(espacos_utilizados)
espaco_medio = espaco_total / len(espacos_utilizados)

with open('relatorio.txt', 'w', encoding="UTF-8") as arquivo_saida:
    arquivo_saida.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")
    arquivo_saida.write("------------------------------------------------------------------------\n")
    arquivo_saida.write("Nr.  Usuário        Espaço utilizado     % do uso\n")

    for i, espaco in enumerate(espacos_utilizados, start=1):
        usuario = linhas[i - 1].split()[0]
        espaco_mb = converter_bytes_para_mb(espaco)
        percentual = calcular_percentual(espaco, espaco_total)

        arquivo_saida.write(f"{i:<4} {usuario:<15} {espaco_mb:>10.2f} MB {percentual:>15.2f}%\n")

    arquivo_saida.write(f"\nEspaço total ocupado: {converter_bytes_para_mb(espaco_total):.2f} MB\n")
    arquivo_saida.write(f"Espaço médio ocupado: {converter_bytes_para_mb(espaco_medio):.2f} MB\n")
