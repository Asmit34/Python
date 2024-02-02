from estd_connection import  estd_connection
cursor=estd_connection()
sql = """
DELETE FROM MYSHARE
WHERE SYMBOL = 'OHL'
"""
cursor.execute(sql)
print("data deleted successfully!!")
