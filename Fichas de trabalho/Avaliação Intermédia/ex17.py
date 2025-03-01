import sqlite3  
conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM funcionários WHERE nome = 'Mariana Costa'")
cursor.execute("DELETE FROM funcionários WHERE salario < 3000")

conn.commit()
conn.close()