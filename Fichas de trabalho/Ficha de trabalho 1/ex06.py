#Faz um programa que receba três parâmetros inteiros (horas, minutos e segundos) e converta o resultado para segundos, devolvendo o output para o ecrã
h = int(input('horas: '))
m = int(input('minutos:'))
s = int(input('segundos:'))
print (f'{h*3600+m*60+s} segundos')
