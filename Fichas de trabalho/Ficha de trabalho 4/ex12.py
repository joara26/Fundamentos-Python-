#. Escreve um programa que calcule e escreva o resultado do fatorial de um número inteiro positivo N
# sabendo que: n!=1*2*3*…*n.
def fatorial(N):
    resultado = 1
    while N > 1:
        resultado *= N
        N -= 1
    return resultado

# Solicitar ao usuário o número N
numero = int(input("Digite um número inteiro positivo: "))

# Verificar se o número é válido
if numero < 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    # Calcular o fatorial e exibir o resultado
    print(f"O fatorial de {numero} é {fatorial(numero)}")

    
