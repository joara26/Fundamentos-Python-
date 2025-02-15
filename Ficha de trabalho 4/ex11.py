# Escreve um programa que calcule a soma e o produto dos N primeiros números naturais.
n = int(input('Digite um número: '))
soma = 0
produto = 1
while n > 0:
    soma += n
    produto *= n 
    n -= 1
    print(soma)