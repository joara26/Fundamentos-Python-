# Escreve um programa que coloque no ecrã a tabuada do número 5.
n = int(input('Digite o número que gostaria de saber a tabuada: '))
i = 0
print(f'tabuada do {n}:')
while i <= 10:
    print(f'{n} x {i} = {n * i}')
    i += 1
    