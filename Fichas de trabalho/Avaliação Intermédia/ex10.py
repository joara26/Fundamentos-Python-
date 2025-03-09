'''Modificar o programa anterior para acrescentar mais uma linha ao ficheiro'''
with open("novo_ficheiro.txt", "a") as ficheiro:
 ficheiro.write("Linha adicional\n")