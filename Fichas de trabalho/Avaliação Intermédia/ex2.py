'''Peça dois números ao utilizador e trate a divisão por zero.'''   
try:
    n1 = int(input('Digite um número: ')) #pedir ao utilizador que digite os 2 numeros separadamente
    n2 = int(input('Digite outro número: '))
    d = n1 / n2  #fórmula da divisão
    print (f'A divisão de {n1} por {n2} é {d}') #resultado básico da divisão 
except ZeroDivisionError:
    print('Erro!! É impossível dividir por zero') #erro caso peça divisão por 0
except ValueError:
    print('São permitidos apenas número inteiros') #erro caso não digite números inteiros