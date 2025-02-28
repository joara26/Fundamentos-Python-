'''A empresa DataSecure precisa de um sistema que copie ficheiros binários de forma
eficiente e segura. Para garantir a integridade dos dados, o sistema deve:
a) Solicitar o nome de um ficheiro binário (ex.: imagem, PDF, áudio) que o
utilizador deseja copiar.
b) Criar uma cópia exata desse ficheiro, preservando os dados originais.
c) Verificar se a cópia foi bem-sucedida, comparando os conteúdos dos dois
ficheiros através do cálculo de um hash MD5.
d) Exibir uma mensagem de sucesso ou erro informando se os ficheiros são
idênticos.'''

import hashlib


def calcular_hash_md5(ficheiro):
    hash_md5 = hashlib.md5()
    with open(ficheiro, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def copiar_ficheiro_binario():
    try:
        nome_origem = input("Digite o nome do ficheiro binário a copiar: ")
        nome_destino = input("Digite o nome do ficheiro de destino: ")

        with open(nome_origem, 'rb') as origem, open(nome_destino, 'wb') as destino:
            destino.write(origem.read())

        hash_origem = calcular_hash_md5(nome_origem)
        hash_destino = calcular_hash_md5(nome_destino)

        if hash_origem == hash_destino:
            print("Cópia realizada com sucesso. Os ficheiros são idênticos.")
        else:
            print("Erro: Os ficheiros não são idênticos.")
    except FileNotFoundError:
        print("Erro: O ficheiro original não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")