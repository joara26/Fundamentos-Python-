import sqlite3
conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

#Atualizar o salário de Pedro Santos
cursor.execute("UPDATE funcionários SET salario = 3000.00 WHERE nome = 'Pedro Santos'")
cursor.execute("UPDATE funcionários SET salario = salario * 1.05")
conn.commit()
conn.close()