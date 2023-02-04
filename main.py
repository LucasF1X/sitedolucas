from flask import Flask, render_template

app = Flask(__name__)

# route
# funcao

@app.route("/")
def homepage():
        return render_template("homepage.html")

@app.route("/contatos")
def contatos():
        return render_template("contatos.html")

@app.route("/ursuarios/<nome_ursuario>")
def ursuarios(nome_ursuario):
        return render_template("ursuarios.html", nome_ursuario=nome_ursuario)



# colocar site no ar
if __name__ == "__main__":
        app.run(debug=True)

        # servidor do heroku
        