'''Escreve uma função em Python que dada uma palavra retorne o número de vogais nessa
palavra.'''


def count_vowels(word):
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)

# Exemplo de uso
word_input = input("Digite uma palavra: ")
print(f"Número de vogais: {count_vowels(word_input)}")
