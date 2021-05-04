from flask import Flask, request, jsonify, make_response, render_template

app = Flask(__name__)


@app.route('/hi')
def hi():
    return 'hi'

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()