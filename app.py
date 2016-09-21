from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    return "No hablo queso"

@app.route('/hi')
def hi():
    return 'hi'

@app.route('/bye')
def bye():
    return 'bye'

def foo():
    return "Rodda"

if __name__ == "__main__":
    app.run()
