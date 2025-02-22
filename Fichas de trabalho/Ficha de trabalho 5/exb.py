'''Utilizando estruturas de repetição escreva um programa que mostre os
resultados da tabuada de multiplicação dos números entre 1 e 10, como segue.'''
contador = 1
while contador <= 10:   
    mult = 1
    while mult <= 10: 
        print(f'{contador} x {mult} = {contador * mult}')
        contador += 1
    mult += 1
    