'''Considera a seguinte lista:
nums=[10, 2.5, 7, 11, 7.9, "Python", True,6, 5.8 , "Listas"]
Efetua um programa em python que:
a. Imprima a quantidade de inteiros, floats, strings e boleanos na lista;
b. Efetua a média de todos os valores inteiros na lista.
c. Crie e retorne uma nova lista só com os valores inteiros'''

nums = [10, 2.5, 7, 11, 7.9, "Python", True, 6, 5.8, "Listas"]

# Criando listas filtradas para cada tipo de dado
inteiros = [n for n in nums if isinstance(n, int) and not isinstance(n, bool)]
floats = [n for n in nums if isinstance(n, float)]
strings = [n for n in nums if isinstance(n, str)]
booleanos = [n for n in nums if isinstance(n, bool)]

# Contando os elementos de cada tipo
qtd_inteiros = len(inteiros)
qtd_floats = len(floats)
qtd_strings = len(strings)
qtd_booleanos = len(booleanos)

# Exibir quantidades
print(f"Quantidade de inteiros: {qtd_inteiros}")
print(f"Quantidade de floats: {qtd_floats}")
print(f"Quantidade de strings: {qtd_strings}")
print(f"Quantidade de booleanos: {qtd_booleanos}")

# Cálculo da média dos inteiros
if qtd_inteiros > 0:
    media = sum(inteiros) / qtd_inteiros
    print(f'A média dos valores inteiros {inteiros} é {media:.2f}')
else:
    print("Não há valores inteiros para calcular a média.")

# Exibir lista de inteiros
print('Lista com valores inteiros:', inteiros)
