#Escreva um programa que peça ao utilizador números entre 0-10. Se o utilizador inserir um número
#fora desse intervalo o programa deverá finalizar com uma mensagem personalizada.
n = int(input('Digite um numero entre 0-10: '))
for i in range (0, 11):
    if n >= 11:
        print('Esse número não consta entre 0-10')
