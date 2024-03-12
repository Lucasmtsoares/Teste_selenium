from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index(): 
    return render_template("basic.html")


@app.route("/processing", methods=['POST'])
def analisar_portarias():
    from models.teste import imprimir
    c = imprimir()
        
    return render_template("teste.html", c=c)


if __name__ == "__main__":
    app.run(debug=True)