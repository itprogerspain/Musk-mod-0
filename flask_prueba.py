from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'Hola Mundo!!'


@app.route('/primera')
def template_primera():
    return render_template('primera_pagina.html')


@app.route('/segunda')
def template_segunda():
    return render_template('segunda_pagina.html')






if __name__ == "__main__":
    app.run(debug=True, port=5000)