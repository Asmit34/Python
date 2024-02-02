from estd_connection1 import estd_connection1
cursor = estd_connection1()
cursor.execute("DROP TABLE IF EXISTS MYSHARE")
sql = """
CREATE TABLE students_table(
name CHAR(20),
age INTEGER
);
"""
cursor.execute(sql)
print("Table created successfully.")
