''' Considera o seguinte dicionário, a que cada prato é associado o respetivo
valor em euros:
menu={
"entremeada": 7,
"Sardinha": 6,
"Filetes": 5.5,
"Prego": 7,
"Hamburguer": 5.5
}
Efetua um programa em python que, após instaciar a variável:
a. Devolva o preço do “prego”.
b. Faça o print de todas as chaves do dicionário
c. Acrescente na lista “omolete” com o preço de 5.
d. Faça o print de todo o dicionário, para visualizar as alterações.
'''
menu={
"entremeada": 7,
"Sardinha": 6,
"Filetes": 5.5,
"Prego": 7,
"Hamburguer": 5.5
}

#Devolva o preço do “prego”
p = menu["Prego"]
print(p)

#print de todas as chaves do dicionário  
print(menu.keys())

#acrescentar na lista 'omolete' com o preço 5
menu ["Omolete"] = 5

#print final para visualizar as alterações
for x, y in menu.items():
    print(x, y)