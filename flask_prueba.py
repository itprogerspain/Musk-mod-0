from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!!'


@app.route('/first')
def template_first():
    return render_template('first_page.html')


@app.route('/second')
def template_second():
    return render_template('second_page.html')






if __name__ == "__main__":
    app.run(debug=True, port=5000)