#. Escreva um programa que peça ao utilizador 20 números reais e no final mostre a soma e a média
#dos números introduzidos.
# Inicializar as variáveis para a soma dos números
soma = 0

# Solicitar 20 números reais ao usuário
for i in range(1, 21):
    numero = float(input(f"Digite o {i}º número real: "))
    soma += numero

# Calcular a média
media = soma / 20

# Exibir a soma e a média
print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media}")
