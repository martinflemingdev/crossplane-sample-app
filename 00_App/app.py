from flask import render_template
from flask import Flask
from db import query_rds
import traceback

app = Flask(__name__)
hostname = "<hostname>"
dbname = "SampleAppDB"
user = "adminuser"
password = "<password>"
query = "SELECT * FROM table_name;"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/app')
def path():
    return "\n\nHello, from App Path!\n\n"

@app.route('/rds')
def db_query():
    try:
        result = query_rds(hostname, dbname, user, password, query)
        return str(result)
    except:
        return str(traceback.format_exc())


if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=8081)