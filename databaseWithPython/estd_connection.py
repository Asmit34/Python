import psycopg2
def estd_connection():
    conn = psycopg2.connect(
        database="share",
        user="postgres",
        password="postgres",
        host="127.0.0.1",
        port="5432"


)
    conn.autocommit = True
    print("Connection establish successfully")
    cursor = conn.cursor()
    return cursor
