'''Considera a lista:
cores=["amarelo", "azul", "branco", "preto", "verde"]
Cria um programa, em python, que:
a. Faz o print de toda a lista
b. Faz o print do indíce 2 da lista
c. Altera o indíce 0 da lista para "vermelho"
d. Faz o print de toda a lista
e. Acrescenta no final da lista a cor "amarelo"
f. Faz o print de toda a lista
g. Acrescenta no indíce 2 a cor "roxo"
h. Faz o print de toda a lista
i. Apaga o último elemento da lista
j. Faz o print de toda a lista
k. Faz o print do tamanho da lista (len)'''
cores=["amarelo", "azul", "branco", "preto", "verde"]
#Faz o print de toda a lista
print(cores)
#Faz o print do indíce 2 da lista
print(cores[2])
#Altera o indíce 0 da lista para "vermelho"
cores[0] = 'vermelho'
#Faz o print de toda a lista
print(cores)
#Acrescenta no final da lista a cor "amarelo"
cores.append('amarelo')
#Faz o print de toda a lista
print(cores)
#Acrescenta no indíce 2 a cor "roxo"
cores[2]='roxo'
#Faz o print de toda a lista
print(cores)
#Apaga o último elemento da lista
cores.pop()
# Faz o print de toda a lista
print(cores)
#Faz o print do tamanho da lista (len)
print(len(cores))