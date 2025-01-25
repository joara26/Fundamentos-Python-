#Faz um programa que receba a distância em km e a quantidade em litros de combustível consumido por um carro num percurso. Calcula o consumo km/l e escreve uma mensagem de acordo com o resultado obtido
#se o consumo for amior que 5, escreve uma mensagem a dizer que o carro é neutro
#se o consumo for menor que 5, escreve uma mensagem a dizer que o carro é económico
km = float(input(' Distância percorrida, em km, pelo carro é:'))
l = float(input('consumo do carro em litros é :'))
consumo = km / l
if consumo > 5:
    print('o carro é neutro')
if consumo <5:
    print('o carro é económico')
