'''Escreve um programa que, dada a sequencia de numeros inteiros (todos fornecidos na mesma linha, separados por espaços), imprima a media desses numeros'''


# Solicita ao usuário que insira os números na mesma linha, separados por espaços
numeros = input("Digite uma sequência de números inteiros separados por espaço: ")

# Converte a entrada em uma lista de inteiros
lista_numeros = list(map(int, numeros.split()))

# Calcula a média
if lista_numeros:  # Verifica se a lista não está vazia
    media = sum(lista_numeros) / len(lista_numeros)
    print(f"A média dos números fornecidos é: {media:.2f}")
else:
    print("Nenhum número foi fornecido.")
