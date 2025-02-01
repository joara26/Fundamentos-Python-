#Escreve um programa que solicite um número inteiro ao utilizador e verifique se o mesmo é par ou ímpar. A mensagem no ecrã deverá ter o seguinte formato;
n = int (input('digite um numero: '))
if n % 2 == 0:
    print(f'o numero {n} é par')
else : 
    print (f'o número {n} é impar')