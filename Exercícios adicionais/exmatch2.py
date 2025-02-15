''' escreva um programa que solicite ao utilizador dois numeros inteiros a operação matemática terá que ser (+,-,*,/) '''
op = input('escolha uma operação: (+,*,/,-)')
num1 = int(input('digite um numero: '))
num2 = int(input('digite um numero: '))
match op:
    case "+":
        rf = num1 + num2
        print(f'A soma de {num1} com {num2} é igual a {rf}')
    case "-":
        rf = num1 - num2 
        print(f'A subtração de {num1} sobre {num2} é igual a {rf}')
    case "*":
        rf = num1 * num2
        print(f'A multiplicação de {num1} com {num2} é igual a {rf}')
    case "/":
        if num2 == 0: 
             rf = False
             print('não é possível fazer a divisão por 0')
        else :
            rf = num1 / num2 
            print(f'A divisão de {num1} sobre {num2} é igual a {rf}')
    case _:
        print('A operação não existe')