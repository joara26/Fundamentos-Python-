'''Escreva um programa que gere 100 números reais aleatórios entre 0 e 1 e
armazene-os numa lista. No final o programa deverá mostrar as seguintes
informações:
i. Maior número;
ii. Menor número;
iii. Soma de todos os números gerados;
iv. Média e desvio padrão.'''
from random import random
from statistics import mean, stdev 

lista = []
for num in range (1, 101):
    lista.append (random()) 
print (f'O maior numero: {max(lista)}')
print(f'o menor número: {min(lista)}')
print(f'a soma dos números: {sum(lista)}')
print(f'media dos numeros gerados: {mean(lista)}')
print(f'a média e os desvio padrão: {stdev(lista)}')