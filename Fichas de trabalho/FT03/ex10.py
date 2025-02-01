#Implemente uma calculadora simples com as operações aritméticas básicas. O utilizador
#deverá especificar a operação desejada (+,-,*,/) e, em seguida, inserir dois valores.
#Caso, o utilizador escolha divisão e insira como valor do denominar 0 mostra uma
#mensagem personalizada. Para os restantes casos, mostra no ecrã o resultado da
#operação desejada.
import math
def calculadora():
    print("Escolha uma operação (+, -, *, /):")
    operacao = input()
    
    if operacao not in ['+', '-', '*', '/']:
        print("Operação inválida!")
        return
    
    print("Digite o primeiro valor:")
    valor1 = float(input())
    
    print("Digite o segundo valor:")
    valor2 = float(input())
    
    if operacao == '+':
        resultado = valor1 + valor2
    elif operacao == '-':
        resultado = valor1 - valor2
    elif operacao == '*':
        resultado = valor1 * valor2
    elif operacao == '/':
        if valor2 == 0:
            print("Erro: Não é possível dividir por zero!")
            return
        else:
            resultado = valor1 / valor2
    
    print(f"O resultado de {valor1} {operacao} {valor2} é: {resultado}")

# Chama a função para iniciar a calculadora
calculadora()
