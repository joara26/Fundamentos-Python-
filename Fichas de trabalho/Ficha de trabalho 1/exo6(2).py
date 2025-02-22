#Escreve um programa que solicite a temperatura em Fahrenheit (F), ao utilizador, e a converta para grau Celsius (C), devolvendo o resultado da conversão.
#formula C = 5 * ((F-32)/9)
F = input ('Digite uma temperatura em Fahrenheit: ')
F = float (F)
C = 5 * ((F-32)/9)
print (f'a temperatura em Celsius é {C:.2f}')