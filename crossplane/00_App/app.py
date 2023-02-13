from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "\n\nHello, from Root Path!\n\n"

@app.route('/app')
def path():
    return "\n\nHello, from App Path!\n\n"


if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=8081)