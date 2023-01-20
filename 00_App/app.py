from flask import render_template
from flask import Flask
from db import query_rds
import traceback, os
from dotenv import load_dotenv

load_dotenv() 
app = Flask(__name__)
hostname = os.getenv('host')
dbname = os.getenv('database')
user = os.getenv('user')
password = os.getenv('password')
port = os.getenv('port')
query = "SELECT * FROM test;"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/app')
def path():
    return "\n\nHello, from App Path!\n\n"

@app.route('/rds')
def db_query():
    try:
        result = query_rds(hostname, dbname, port, user, password, query)
        return str(result)
    except:
        return str(traceback.format_exc())


if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=8081)