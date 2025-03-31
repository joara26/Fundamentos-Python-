'''Utilizando a biblioteca NumPy :
a. Cria um array de números 1 com shape (8, 2)
b. Cria um array de zeros com shape (5, 7)
c. Subtraia o novo array de outro com dados aleatórios e armazene o numa variável
chamada subarray
d. Calcula a média dos valores do array subarray'''


import numpy as np

def extract_date_parts(date_str):
    try:
        day, month, year = map(int, date_str.split("/"))
        return day, month, year
    except ValueError:
        print("Formato inválido. Use DD/MM/AAAA.")
        return None

def count_vowels(word):
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)

def process_numbers(numbers):
    try:
        total = sum(numbers)
        count = len(numbers)
        average = total / count if count > 0 else 0
    except TypeError:
        print("A lista deve conter apenas números.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    else:
        print(f"Soma: {total}, Número de elementos: {count}, Média: {average}")
    finally:
        print("Processamento concluído.")

# Criando arrays com NumPy
array_ones = np.ones((8, 2))
array_zeros = np.zeros((5, 7))
random_array = np.random.rand(5, 7)
subarray = array_zeros - random_array
media_subarray = np.mean(subarray)

# Exibindo resultados
print("Array de uns:")
print(array_ones)
print("\nArray de zeros:")
print(array_zeros)
print("\nSubarray:")
print(subarray)
print("\nMédia dos valores do subarray:", media_subarray)

# Exemplo de uso
date_input = input("Digite uma data no formato DD/MM/AAAA: ")
date_parts = extract_date_parts(date_input)

if date_parts:
    day, month, year = date_parts
    print(f"Dia: {day}, Mês: {month}, Ano: {year}")

word_input = input("Digite uma palavra: ")
print(f"Número de vogais: {count_vowels(word_input)}")

try:
    numbers_input = list(map(float, input("Digite uma lista de números separados por espaço: ").split()))
    process_numbers(numbers_input)
except ValueError:
    print("Entrada inválida. Certifique-se de inserir apenas números.")
