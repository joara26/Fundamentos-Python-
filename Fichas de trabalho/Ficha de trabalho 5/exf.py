'''f. Escreve um programa, em python, que verifique se uma lista é vazia ou não.
Caso a lista seja vazia, mostre True, caso contrário False.'''
def lista_vazia(lista):
    return not lista

# Testes
print(lista_vazia([]))  # True
print(lista_vazia([1, 2, 3]))  # False
