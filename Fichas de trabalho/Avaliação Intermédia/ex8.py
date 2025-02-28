'''Modificar o exercício anterior para exibir o conteúdo linha por linha.'''
nome_ficheiro = input("Digite o nome do ficheiro de texto: ")
open(nome_ficheiro, 'r')
for linha in nome_ficheiro:
        print(linha.strip())