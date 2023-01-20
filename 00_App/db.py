def query_rds(hostname, dbname, user, password, query):
    import psycopg2
    conn = psycopg2.connect(
        database="my-rds-table-name",
        user="my_user_name",
        password="",
        host="my-rds-table-name.123456.us-east-1.rds.amazonaws.com",
        port='5432'
    )
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows


# python3 -m pip install boto3
# python3 -m pip install psycopg2-binary==2.9.5
# python3 -m pip install pandas
def create_table():
    import psycopg2
    import pandas as pd
    conn = psycopg2.connect(database="SampleAppDB",user="adminuser",password='',host="rds-sample-app-instance.cslbyggrhpq2.us-east-1.rds.amazonaws.com",port='5432')
    cur = conn.cursor()
    cur.execute("CREATE TABLE test (id serial PRIMARY KEY, name varchar, data varchar);")
    conn.commit() 

    postgres_insert_query = """ INSERT INTO test (name, data) VALUES (%s,%s)"""
    record_to_insert = ('Martin', "Successful Demo!")
    cur.execute(postgres_insert_query, record_to_insert)
    conn.commit() 
    conn.close()
    cur.close()