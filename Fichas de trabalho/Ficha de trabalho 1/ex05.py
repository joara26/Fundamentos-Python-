#Sejam a e b os catetos de um triângulo retângulo, faz um programa que devolva o valor da hipotenusa
#raiz quadrada na math é hypot
from math import hypot 
a = int (input ('digite o valor do cateto a:'))
b = int (input ('digite o valor do cateto b:'))
h = hypot (a , b )
print ('o valor da hipotenusa é : ',format (h))

