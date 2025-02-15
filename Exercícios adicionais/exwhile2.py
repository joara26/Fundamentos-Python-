'''escreve um programa que utilize a instrução while, que devolva a tabuada do 8'''
numero = 8 #dar o valor da tabuada
contador = 1 #dar o valor real do contador que neste caso tem de começar por 1 e não por 0
while contador <=10 :
    resultado = numero * contador
    print(f'{numero} x {contador} = {resultado}')
    contador += 1