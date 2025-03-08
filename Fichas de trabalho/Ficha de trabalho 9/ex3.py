''' Efetua um programa em python:
a. Instancie o seguinte dicionário:
Computadores_1={
 "Marca":"Asus",
 "Ecra":"14Pol",
 "RAM": [4, 8, 12]
 }
b. Acrescente um novo elemento à lista com chave igual a “Disco” e
valor [“128G”, “256G”]
c. Permita ao utilizador introduzir um valor específico de RAM e
verificar se esta está presente na lista.
d. Acrecente 16 como novo valor de RAM.
e. Copie o dicionário para um novo usando Deep Copy().
f. Na lista nova modifique a marca para “Lenovo” e os valores da RAM
para [4,8]. Imprima a nova lista
g. Crie uma nova lista com deep copy e modifique a marca para “HP” e
Disco para [“256G”]- Imprima a respetiva lista
h. Cria uma lista cujos elementos são os três dicionários.
i. Imprima as marcas com 128G de RAM
j. Imprima as marcas com 8 e 12 de RAM'''

import copy

Computadores_1={
 "Marca":"Asus",
 "Ecra":"14Pol",
 "RAM": [4, 8, 12]
}

#Acrescente um novo elemento à lista com chave igual a “Disco” e valor 128G 256G
Computadores_1 ["Disco"] = "128G" , "256G"

#Pedir ao utilizador um valor específico de Ram
valor_ram = int(input('Digite o valor da Ram que procura: '))

# Verifica se o valor está na lista
if valor_ram in Computadores_1["RAM"]:
    print(f"O valor {valor_ram}GB está disponível na lista de RAM.")
else:
    print (f"Erro: O valor {valor_ram}GB não está disponível na lista de RAM.")

#Acrescentar 16 como novo valor da RAM
Computadores_1 ["RAM"] = [4, 8, 12, 16]

#Copie o dicionário para um novo usando Deep Copy().
Computadores_2 = copy.deepcopy(Computadores_1)


#Na lista nova modifique a marca para “Lenovo” e os valores da RAM para [4,8]. Imprima a nova lista
Computadores_2 ["Marca"] = "Lenovo"
Computadores_2 ["RAM"] = [4, 8]
print('Dicionário 2: ', Computadores_2)
    

#Crie uma nova lista com deep copy e modifique a marca para “HP” e Disco para [“256G”]- Imprima a respetiva lista
Computadores_3 = copy.deepcopy(Computadores_1)
Computadores_3 ["Marca"] = "HP"
Computadores_3 ["Disco"] = ["256G"]
print('Dicionário 3:' ,Computadores_3)

#Cria uma lista cujos elementos são os três dicionários
lista_dicionarios = [Computadores_1, Computadores_2, Computadores_3]

#Imprime as marcas com 128G de RAM
print("Marcas com 128G de Disco:")
for computador in lista_dicionarios:
    if "128G" in computador.get("Disco", []):
        print(computador["Marca"])

#Imprime as marcas com 8 e 12 de RAM
print("Marcas com 8 e 12 de RAM:")
for computador in lista_dicionarios:
    if 8 in computador["RAM"] and 12 in computador["RAM"]:
        print(computador["Marca"])
