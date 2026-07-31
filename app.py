from flask import Flask, render_template, request, session, redirect
from palavras import escolher_palavra, palavra_existe

app = Flask(__name__)

app.secret_key = "descobre_palavra_2026"



def verificar(tentativa, resposta):

    resultado = ["⬜"] * 5

    resposta_lista = list(resposta)


    # Letras certas no sítio certo
    for i in range(5):

        if tentativa[i] == resposta[i]:

            resultado[i] = "🟩"
            resposta_lista[i] = None



    # Letras certas no sítio errado
    for i in range(5):

        if resultado[i] == "⬜":

            if tentativa[i] in resposta_lista:

                resultado[i] = "🟨"

                resposta_lista[
                    resposta_lista.index(tentativa[i])
                ] = None


    return resultado





@app.route("/", methods=["GET", "POST"])
def inicio():


    # Forçar novo jogo
    if request.args.get("novo") == "1":

        session.clear()

        return redirect("/")



    # Criar jogo se não existir

    if "palavra" not in session or "tentativas" not in session:

        session.clear()

        session["palavra"] = escolher_palavra()

        session["tentativas"] = []

        session["fim"] = False

        session["mensagem"] = ""



    palavra = session["palavra"]

    tentativas = session["tentativas"]

    mensagem = session.get("mensagem", "")



    if request.method == "POST":



        # Botão NOVO JOGO

        if request.form.get("novo_jogo"):

            session.clear()

            return redirect("/")




        # Se o jogo terminou

        if session.get("fim"):

            return redirect("/")




        tentativa = request.form.get("palavra", "").lower()



        if len(tentativa) != 5:


            mensagem = "A palavra tem de ter 5 letras!"



        elif not palavra_existe(tentativa):


            mensagem = "Essa palavra não existe!"



        else:



            resultado = verificar(

                tentativa,

                palavra

            )


            linha = []



            for i in range(5):


                if resultado[i] == "🟩":

                    cor = "verde"


                elif resultado[i] == "🟨":

                    cor = "amarelo"


                else:

                    cor = "cinza"



                linha.append(

                    (

                        tentativa[i].upper(),

                        cor

                    )

                )



            tentativas.append(linha)



            session["tentativas"] = tentativas



            if tentativa == palavra:


                session["fim"] = True

                session["mensagem"] = "🎉 Parabéns! Acertaste!"



            elif len(tentativas) >= 6:


                session["fim"] = True

                session["mensagem"] = (

                    "😢 Fim do jogo! A palavra era "

                    + palavra.upper()

                )



            else:


                session["mensagem"] = ""



            session.modified = True


            # Evita duplicar no F5

            return redirect("/")



    return render_template(

        "index.html",

        tentativas=tentativas,

        mensagem=mensagem

    )






if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )