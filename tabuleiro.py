def mostrar_tabuleiro(tentativas):

    print("\n")

    for linha in tentativas:

        print(" ".join(linha))

    for _ in range(6 - len(tentativas)):

        print("⬜ ⬜ ⬜ ⬜ ⬜")

    print()