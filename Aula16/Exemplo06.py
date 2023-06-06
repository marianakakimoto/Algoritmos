def entrada():
    try:
        n1 = int(input("Informe um número: "))
    except ValueError:
        return None
    else:
        print(f"Você digitou o {n1}")
    finally:
        print("Fim da execução...")

entrada()
