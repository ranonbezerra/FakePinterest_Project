from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/profile')
def profile():
    return 'User Profile'

if __name__ == '__main__':
    app.run(debug=True)