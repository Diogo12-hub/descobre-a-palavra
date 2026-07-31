from palavras import escolher_palavra, palavra_existe, remover_acentos
from tabuleiro import mostrar_tabuleiro


def verificar(tentativa, resposta):
    resultado = ["⬜"] * 5
    resposta_lista = list(resposta)

    # Letras certas no lugar certo
    for i in range(5):
        if tentativa[i] == resposta[i]:
            resultado[i] = "🟩"
            resposta_lista[i] = None

    # Letras certas no lugar errado
    for i in range(5):
        if resultado[i] == "⬜":
            if tentativa[i] in resposta_lista:
                resultado[i] = "🟨"
                resposta_lista[resposta_lista.index(tentativa[i])] = None

    return resultado


def jogar():
    print("=" * 30)
    print("       TERMO PORTUGUÊS")
    print("=" * 30)

    palavra = escolher_palavra()

    tentativas_max = 6
    tentativas = 0

    tabuleiro = []

    while tentativas < tentativas_max:

        tentativa = input(f"\nTentativa {tentativas + 1}/6: ").lower()
        tentativa = remover_acentos(tentativa)

        # Confirmar tamanho
        if len(tentativa) != 5:
            print("A palavra tem de ter 5 letras!")
            continue

        # Confirmar se existe
        if not palavra_existe(tentativa):
            print("Essa palavra não existe!")
            continue

        # Verificar tentativa
        resultado = verificar(tentativa, palavra)

        # Adicionar ao tabuleiro
        tabuleiro.append(resultado)

        # Mostrar tabuleiro
        mostrar_tabuleiro(tabuleiro)

        palavra = remover_acentos(escolher_palavra())

        tentativas += 1

        # Vitória
        if tentativa == palavra:
            print("\n🎉 Parabéns! Acertaste!")
            return

    # Derrota
    print("\n😢 Fim do jogo!")
    print("A palavra era:", palavra)


if __name__ == "__main__":
    jogar()