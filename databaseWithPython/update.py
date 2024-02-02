from estd_connection import estd_connection
cursor = estd_connection()
sql = """
UPDATE MYSHARE SET
NAME='Butwal Power Company'                                                                                           
WHERE SYMBOL = 'BPCL'

"""
cursor.execute(sql)
print("Table updated successfully.")