#Escreva um programa que verifique se um determinado número introduzido pelo utilizador é nulo, positivo ou negativo.
n1 = float(input('digite um numero: '))
if n1 == 0:
    print('o numero é nulo')
elif n1 > 0:
    print('o numero é positivo')
else :
    print('o numero é negativo')