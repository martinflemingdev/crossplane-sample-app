import psycopg2

def create_table(hostname, dbname, port, user, password):
    conn = psycopg2.connect(
        database=dbname,
        user=user,
        password=password,
        host=hostname,
        port=port
    )
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS testing; CREATE TABLE testing (id serial PRIMARY KEY, test varchar, data varchar);")
    conn.commit()
    postgres_insert_query = ''' INSERT INTO testing (test, data) VALUES (%s,%s)'''
    record_to_insert = ('It','worked!')
    cursor.execute(postgres_insert_query, record_to_insert)
    conn.commit()
    conn.close()
    cursor.close()

def query_rds(query, hostname, dbname, port, user, password):
    conn = psycopg2.connect(
        database=dbname,
        user=user,
        password=password,
        host=hostname,
        port=port
    )
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    cur.close()
    return rows

def hanlder(event, context=None):
    hostname=event['hostname']
    dbname=event['dbname']
    user=event['user']
    password=event['password']
    port=event['port']
    create_table(hostname, dbname, port, user, password)
    query = "SELECT * FROM testing;"
    result = query_rds(query, hostname, dbname, port, user, password)
    return f"{str(result)}"