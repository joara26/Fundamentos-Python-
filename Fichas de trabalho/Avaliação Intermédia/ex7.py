'''Criar um programa que leia um ficheiro de texto e exibir o seu conteúdo'''
try:
        nome_ficheiro = input("Digite o nome do ficheiro de texto: ")
        with open(nome_ficheiro, 'r', encoding='utf-8') as ficheiro:
            conteudo = ficheiro.read()
            print("Conteúdo do ficheiro:")
            print(conteudo)
except FileNotFoundError:
        print("Erro: O ficheiro não foi encontrado.")
except Exception as e:
        print(f"Ocorreu um erro: {e}")