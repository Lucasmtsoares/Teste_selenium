from flask import Flask, render_template
from api import app



@app.route("/")
def index(): 
    return render_template("basic.html")

@app.route("/processing", methods=['POST'])
def analisar_portarias():
    
        
    return render_template("teste.html")
