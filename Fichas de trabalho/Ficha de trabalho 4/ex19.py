'''Escreve um programa que solicite ao utilizador um número e escreva em simultâneo a sequência
crescente e decrescente entre 1 e esse número.
Apresentação no ecrã:
1 5
2 4
3 3
4 2
5 1'''
# Solicitar ao usuário um número
n = int(input("Digite um número: "))

# Gerar a sequência crescente (1 até n) e decrescente (n até 1)
for i in range(1, n, 1):
    print(i, n - i + 1)
