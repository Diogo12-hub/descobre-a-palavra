import unicodedata


def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize("NFD", texto.lower())
        if unicodedata.category(c) != "Mn"
    )


palavras = set()


with open("dicionario/pt_PT.dic", encoding="utf-8") as ficheiro:

    # ignorar primeira linha (quantidade de palavras)
    next(ficheiro)

    for linha in ficheiro:

        palavra = linha.strip()

        # ignorar linhas vazias
        if not palavra:
            continue

        # tirar regras do Hunspell
        if "/" in palavra:
            palavra = palavra.split("/")[0]

        # tirar acentos
        palavra = remover_acentos(palavra)

        # guardar apenas palavras de 5 letras
        if len(palavra) == 5 and palavra.isalpha():
            palavras.add(palavra)


with open("palavras.txt", "w", encoding="utf-8") as ficheiro:

    for palavra in sorted(palavras):
        ficheiro.write(palavra + "\n")


print("Foram guardadas", len(palavras), "palavras.")