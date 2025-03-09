'''Cria um menu interativo para gerir a base de dados, onde o utilizador pode escolher entre:
-Adicionar um novo funcionário 
-Listar todos os funcionários
-Atualizar o salário de um funcionário
-Eliminar um funcionário
-Sair'''
import sqlite3

def criar_tabela():
    """Cria a tabela se ela não existir."""
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS funcionarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cargo TEXT NOT NULL,
            salario REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def menu():
    """Exibe o menu interativo."""
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()

    while True:
        print("\nMENU DE GESTÃO DE FUNCIONÁRIOS")
        print("1. Adicionar funcionário")
        print("2. Listar funcionários")
        print("3. Atualizar salário")
        print("4. Eliminar funcionário")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            cargo = input("Cargo: ")
            salario = float(input("Salário: "))
            cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)", (nome, cargo, salario))
            conn.commit()
            print("Funcionário adicionado com sucesso!")

        elif opcao == '2':
            cursor.execute("SELECT * FROM funcionarios")
            funcionarios = cursor.fetchall()
            if funcionarios:
                print("\nLista de Funcionários:")
                for funcionario in funcionarios:
                    print(f"ID: {funcionario[0]}, Nome: {funcionario[1]}, Cargo: {funcionario[2]}, Salário: {funcionario[3]}")
            else:
                print("Nenhum funcionário encontrado.")

        elif opcao == '3':
            nome = input("Nome do funcionário: ")
            novo_salario = float(input("Novo salário: "))
            cursor.execute("UPDATE funcionarios SET salario = ? WHERE nome = ?", (novo_salario, nome))
            conn.commit()
            if cursor.rowcount > 0:
                print("Salário atualizado com sucesso!")
            else:
                print("Funcionário não encontrado.")

        elif opcao == '4':
            nome = input("Nome do funcionário: ")
            cursor.execute("DELETE FROM funcionarios WHERE nome = ?", (nome,))
            conn.commit()
            if cursor.rowcount > 0:
                print("Funcionário removido com sucesso!")
            else:
                print("Funcionário não encontrado.")

        elif opcao == '5':
            conn.close()
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")

# Criar a tabela antes de iniciar o menu
criar_tabela()
menu()