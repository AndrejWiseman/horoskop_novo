from flask import Flask, render_template
from horoskop import blizanci, vodolija

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/blizanci')
def bliz():
    return blizanci()

@app.route('/vodolija')
def vodo():
    return vodolija()


if __name__ == '__main__':
    app.run()
