#Escreve um programa que receba dois números reais e indique qual o maior dos dois números. Considera a possibilidade de o utilizador indicar dois números iguais.
n1 = float(input('digite um numero: '))
n2 = float(input('digite outro numero: '))
if n1 > n2 :
    print(f'{n1} é maior que o {n2}')
elif n1 < n2 :
    print(f'{n2} é maior que o {n1}')
else :
    print('os numeros são iguais')