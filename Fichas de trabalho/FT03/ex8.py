#Escreve um programa para classificar um triângulo de acordo com o comprimento dos
#seus lados. Considere as seguintes informações
l1 = float(input('digite o numero do lado 1: '))
l2 = float(input('digite o numero do lado 2: '))
l3 = float(input('digite o numero do lado 3: '))
if l1 == l2 and l2 == l3 :
    print('o triângulo é equilátero')
elif l1 < l2 and l2 == l3 :
    print('o triângulo é isósceles')
else :
    print('o triângulo é escaleno')
