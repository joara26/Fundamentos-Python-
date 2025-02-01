#Escreve um programa que receba três números reais distintos e indique qual o maior dos três números.
n1 = float(input('digite um numero: '))
n2 = float(input('digite outro numero: '))
n3 = float(input('digite outro numero: '))
if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior numero')
elif n2 > n1 and n2 > n3:
    print(f'{n2} é o maior numero')
else:
    print(f'{n3} é o maior numero')