import psycopg2

def query_rds(hostname, dbname, port, user, password, query):
    conn = psycopg2.connect(
        database=dbname,
        user=user,
        password=password,
        host=hostname,
        port=port
    )
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    cursor.close()
    return rows

# python3 -m pip install psycopg2-binary==2.9.5

def create_table(hostname, dbname, port, user, password):
    conn = psycopg2.connect(
        database=dbname,
        user=user,
        password=password,
        host=hostname,
        port=port
    )
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS test; CREATE TABLE test (id serial PRIMARY KEY, name varchar, data varchar);")
    conn.commit() 

    postgres_insert_query = """ INSERT INTO test (name, data) VALUES (%s,%s)"""
    record_to_insert = ('Martin', "Successful Demo!")
    cursor.execute(postgres_insert_query, record_to_insert)
    conn.commit() 
    conn.close()
    cursor.close()