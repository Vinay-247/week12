from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('myForm.html')

@app.route('/submit', methods=['GET','POST'])
def submit():
    # Get data from the form
    username = request.form['username']
    return render_template('greeting.html', name=username)

from threading import Thread
from app import app  # if your app is in app.py itself, just use `app`

if __name__ == "__main__":
    def run_app():
        app.run(host='0.0.0.0', port=5000, debug=False)  # debug=False avoids reloader issues

    Thread(target=run_app).start()

