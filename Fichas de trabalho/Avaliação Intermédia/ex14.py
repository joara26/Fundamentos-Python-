import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

#inserir funcionários na tabela
cursor.execute("INSERT INTO funcionários (nome, cargo, salario) VALUES ('Ana Silva', 'Gestora', 3500)")
cursor.execute("INSERT INTO funcionários (nome, cargo, salario) VALUES ('Pedro Santos', 'Programador', 4000)")
cursor.execute("INSERT INTO funcionários (nome, cargo, salario) VALUES ('Mariana Costa', 'Designer', 2500)")
cursor.execute("INSERT INTO funcionários (nome, cargo, salario) VALUES ('José Almeida', 'Analista', 3000)")
cursor.execute("INSERT INTO funcionários (nome, cargo, salario) VALUES ('Laura Souza', 'Gerente de Projetos', 4500)")

#Guardar mudanças e fechar conexão
conn.commit()
conn.close()

