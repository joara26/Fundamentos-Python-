'''Crie um programa que captura qualquer erro e exibe uma mensagem
apropriada.'''
import sys 
try:
#Pedir ao utilizador para digitar um número
    num1 = int(input('Digite um número: '))
#Criar uma divisão 
    d = num1 / 2
    print(f'Metade de {num1} é {d}') 
#criação de erro
except Exception as e :
    print('Erro inesperado, digite um número inteiro', e)
    sys.exit(1)
    

