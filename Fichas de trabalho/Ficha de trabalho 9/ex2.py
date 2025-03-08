''' Efetua um programa em python onde:
a. Cries um dicionário e efetues o respetivo print.
b. Acrescentes dois novos elementos ao dicionário.
c. Removes um dos elementos da lista;
d. Efetues uma operação, à escolha, sobre os dados no dicionário'''


carro={
    "Marca": "Mercedes",
    "Modelo": "S45",
    "Ano": "2022"
}
#print do dicionário
print(carro)

#adiciona dois elementos ao dicionário
carro ["Potência"] = 220
carro ["Cor"] = "Branco"

#Remove o elemento "Ano" da lista
del carro ["Ano"]

#Altera o modelo da lista para "AMG"
carro ["Modelo"] = "AMG"
print(carro)