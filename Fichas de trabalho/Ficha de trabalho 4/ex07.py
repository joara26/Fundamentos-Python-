#Elabora um programa para calcula a soma dos N primeiros números naturais (1+2+3+...+N)
#em que N é um número introduzido pelo utilizador (NOTA: este programa poderia ser feito
#utilizando a fórmula da progressão aritmética, S = (1+N) * N/2, mas faz de conta que não
#sabíamos a fórmula).
def soma_numeros(N):
    soma = 0
    contador = 1
    while contador <= N:
        soma += contador
        contador += 1
    return soma

# Solicitar ao usuário o número N
numero = int(input("Digite um número inteiro positivo N: "))

# Verificar se o número é válido
if numero < 1:
    print("Por favor, insira um número inteiro positivo maior ou igual a 1.")
else:
    # Calcular a soma dos N primeiros números naturais e exibir o resultado
    print(f"A soma dos {numero} primeiros números naturais é {soma_numeros(numero)}")
