import psycopg2
def estd_connection1():
    conn = psycopg2.connect(
        database="students",
        user="postgres",
        password="postgres",
        host="127.0.0.1",
        port="5432"


)
    conn.autocommit = True
    print("Connection establish successfully")
    cursor = conn.cursor()
    return cursor
