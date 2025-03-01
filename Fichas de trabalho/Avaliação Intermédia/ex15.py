import sqlite3
conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

#Consultar todos os funcionários
cursor.execute("SELECT * FROM funcionários")
funcionarios = cursor.fetchall()

#Exibir os resultados
for funcionario in funcionarios:
    print(funcionario)
    
conn.close()

#Explicação do código
#conn = sqlite3.connect('empresa.db')
#Esta linha estabelece uma conexão com o banco de dados chamado empresa.db. Se o banco de dados não existir, ele será criado automaticamente.
#A variável conn vai manter a ligação ao banco de dados e é usada para executar comandos SQL.
#cursor = conn.cursor()
#Aqui, estamos a criar um cursor, que é um objeto utilizado para interagir com o banco de dados. O cursor permite enviar comandos SQL (como SELECT, INSERT, UPDATE, etc.) ao banco de dados.
#A variável cursor vai ser usada para executar as consultas SQL e obter os resultados.
#cursor.execute("SELECT * FROM funcionários")
#A instrução SQL SELECT * FROM funcionários é executada usando o cursor.
#O comando SELECT * seleciona todos os campos (* é um asterisco que significa "todos os campos") da tabela chamada funcionários.
#Isto vai buscar todos os dados que estão armazenados na tabela funcionários do banco de dados.
#funcionarios = cursor.fetchall()
#O método fetchall() do cursor recupera todos os resultados da consulta realizada.
#O resultado da consulta, ou seja, todos os funcionários armazenados na tabela, é armazenado na variável funcionarios. Esta variável será uma lista de tuplos, onde cada tuplo representa uma linha da tabela funcionários.
#for funcionario in funcionarios:
#print(funcionario)
#Aqui estamos a usar um loop for para iterar sobre todos os elementos na lista funcionarios.
#Cada elemento da lista funcionarios é um tuplo que contém os dados de um funcionário (por exemplo, o nome, o cargo, o salário, etc.).
#A instrução print(funcionario) exibe os dados de cada funcionário na consola
#conn.close()
#Fecha, por fim, a conexão