'''Verifique se um ficheiro existe antes de o abrir.'''
from pathlib import Path

# Caminho do ficheiro
caminho = Path('caminho/do/ficheiro.txt')

# Verifica se o ficheiro existe
if caminho.exists():
    with open(caminho, 'r') as f:
        conteudo = f.read()
        print(conteudo)
else:
    print("O ficheiro não existe.")
