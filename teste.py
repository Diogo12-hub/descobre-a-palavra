with open("dicionario/pt_PT.dic", encoding="utf-8") as f:
    linhas = f.readlines()

print("Total de linhas:", len(linhas))

for i, linha in enumerate(linhas[:200]):
    print(i, repr(linha))