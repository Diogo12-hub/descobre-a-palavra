import random
import unicodedata


def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize("NFD", texto.lower())
        if unicodedata.category(c) != "Mn"
    )


with open("palavras.txt", encoding="utf-8") as f:
    PALAVRAS = [
        linha.strip()
        for linha in f
        if len(linha.strip()) == 5
    ]


def escolher_palavra():
    return random.choice(PALAVRAS)


def palavra_existe(palavra):
    return remover_acentos(palavra) in PALAVRAS