#Fazer um programa para ler quatro números inteiros e positivos, calcular e devolver a sua
#média.
def ler_numero():
    while True:
        numero = int(input("Digite um número inteiro e positivo: "))
        if numero > 0:
            return numero
        else:
            print("Por favor, insira um número positivo.")

# Ler quatro números inteiros e positivos
numeros = []
for i in range(4):
    numeros.append(ler_numero())

# Calcular a média
media = sum(numeros) / len(numeros)

# Exibir a média
print(f"A média dos números é: {media:.2f}")
