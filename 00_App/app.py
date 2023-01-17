from flask import render_template
from flask import Flask
from db import query_rds

app = Flask(__name__)
hostname = "<hostname>"
dbname = "<dbname>"
user = "<user>"
password = "<password>"
query = "SELECT * FROM table_name;"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/app')
def app():
    return "Hello, from App Path!"

@app.route('/db')
def db():
    result = query_rds(hostname, dbname, user, password, query)
    return result


if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=8081)