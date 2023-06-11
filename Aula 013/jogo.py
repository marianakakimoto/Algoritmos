from funcoes import lancar_dado

def jogar_dados():
    print("Jogo de Dados")
    print("--------------")

    jogador = input("Digite seu nome: ")
    print("Olá,", jogador + "!")

    computador = "Computador"
    print("Seu oponente é o", computador + "!")

    jogar_novamente = True

    while jogar_novamente:
        jogador_resultado = lancar_dado()
        computador_resultado = lancar_dado()

        print("Resultado do lançamento de", jogador + ":", jogador_resultado)
        print("Resultado do lançamento do", computador + ":", computador_resultado)

        if jogador_resultado > computador_resultado:
            print(jogador + " ganhou!")
        elif jogador_resultado < computador_resultado:
            print(computador + " ganhou!")
        else:
            print("Empate!")

        resposta = input("Deseja jogar novamente? (s/n): ")
        jogar_novamente = resposta.lower() == "s"

jogar_dados()
