import sqlite3
#criar conexão com o banco de dados
conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()
#criar tabela de funcionários
cursor.execute('''
               CREATE TABLE IF NOT EXISTS funcionários(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   cargo TEXT NOT NULL,
                   salario REAL NOT NULL
               )
               ''')
#Guardar as mudanças e fechar a conexão
conn.commit()
conn.close()



