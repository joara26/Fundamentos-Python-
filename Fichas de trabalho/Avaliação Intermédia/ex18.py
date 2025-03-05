'''Cria um menu interativo para gerir a base de dados, onde o utilizador pode escolher entre:
-Adicionar um novo funcionário 
-Listar todos os funcionários
-Atualizar o salário de um funcionário
-Eliminar um funcionário
-Sair'''
import sqlite3
from sqlite3 import Cursor


def menu():
    while True:
        print("\nMENU DE GESTÃO DE FUNCIONÁRIOS")
        print("1. Adicionar funcionários")
        print("2. Listar funcionários")
        print("3. Atualizar salário ")
        print("4. Eliminar funcionário")
        print("5.  Sair")
        opcao = input ("Escolha uma opção")
        
        if opcao == '1':
            nome = input("Nome: ")
            cargo = input ("Cargo: ")
            salario = float(input("Salário: "))
            Cursor.execute("INSERT INTO funcionários (nome, cargo, salário) VALUES (?,?,?)") , (nome, cargo, salario)
        elif opcao == '2':
            Cursor.execute("SELECT * FROM funcionários")
            for funcionario in Cursor.fetchall():
                print(funcionario)
        elif opcao == '3':
            nome = input ("Nome do funcionário: ")
            novo_salario = float(input("Novo salário: "))
            Cursor.execute("UPDATE funcionarios SET salario = ? WHERE nome = ?", (novo_salario, nome))
        elif opcao == '4':
            nome = input("Nome do funcionário: ")
            Cursor.execute ("DELETE FROM funcionarios WHERE nome = ?" , (nome,))  
        elif opcao == '5':
            conn.commit()
            conn.close()
            break
        else:
            print("Opção inválida! Tente novamente.")
#criar conexão
conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()
menu()