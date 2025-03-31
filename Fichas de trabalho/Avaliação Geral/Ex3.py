'''Escreve uma função em Python que dada uma lista de números imprime a soma dos
valores dessa lista, o número de elementos da lista e a media desses valores. Implementa
tratamento de exceções no teu código (try…except…else..finally).'''

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
