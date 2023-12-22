from flask import Flask


app = Flask(__name__)

@app.route('/')
def homepage():
    return 'OI SOFIS. AQUI É O NON, O MAIS TOP'


if __name__ == '__main__':
    app.run(debug=True)