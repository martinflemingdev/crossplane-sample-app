import psycopg2

def query_rds(hostname, dbname, user, password, query):
    connect_str = "dbname='{}' user='{}' host='{}' password='{}'".format(dbname, user, hostname, password)
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows