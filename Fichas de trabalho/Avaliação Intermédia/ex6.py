'''Elabora uma script em python que peça ao utilizador dois números e devolva
a divisão do primeiro número introduzido pelo seguinte. Trate erros como
divisão por zero e valores inválidos.'''
while True:
    try:
   #Pedir ao utilizador que insira os números
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite um número: '))
    #fórmula da divisão
        d = num1 / num2 
    #tratamento de erros se dividir por 0
    except ZeroDivisionError:
        print(f'ERRO: É impossível dividir {num1} por 0')
        continue
    #tratamento de erro caso digite um número que não seja inteiro
    except ValueError:
        print('ERRO: Digite apenas números inteiros')
        continue
    print(f'{num1} a dividir por {num2} é {d}')
    break