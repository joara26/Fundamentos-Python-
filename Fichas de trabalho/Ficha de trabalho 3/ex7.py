#Elabora um programa para verificar se um ano é bissexto ou não. A condição para ser
#um ano bissexto é: o ano deve ser divisível por 400; ou se for divisível por 4 e não for
#divisível por 100.
a = int(input('digite o ano: '))
if a % 400 == 0:
    print(f'o ano {a} é bissexto')
else :
    print(f'o ano {a} não é bissexto')
