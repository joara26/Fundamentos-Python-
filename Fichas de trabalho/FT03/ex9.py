'''O Índice de Massa Corporal (IMC) é utilizado para medir o peso ideal de uma pessoa.
Escreve um programa que peça o nome, a idade, o peso e a altura do utilizado e que,
de seguida, calcule e mostre o resultado do seu IMC e classifique esse resultado de
acordo com as seguintes condições:
• IMC<17 - Muito abaixo do peso ideal
• 17<=IMC<18,5 - Abaixo do peso
• 18,5<=IMC<25 - Peso normal
• 25<=IMC<30 - Acima do peso
• 30<=IMC<35 - Obesidade I
• 35<=IMC<40 - Obesidade II (severa)
• IMC>=40 - Obesidade III (mórbida)'''
#Nota: IMC=massa/(altura*altura)

n = str(input('digite o nome: '))
i = int(input('digite a idade: '))
p = float(input('digite o peso: '))
a = float(input('digite a altura: '))
imc = p / (a*a)
if imc < 17 :
    print(f'{n} está muito abaixo do peso ideal')
elif 17<=imc<18.5 :
    print(f'{n} está abaixo do peso')
elif 18.5<=imc<25 :
    print(f'{n} tem o peso normal')
elif 25<=imc<30 : 
    print(f'{n} está acima do peso')
elif 30<=imc<35 :
    print(f'{n} tem obesidade nivel 1')
elif 35<=imc<40 :
    print(f'{n} tem obesidade nivel 2, ou seja, severa')
else : 
    print(f'{n} tem obesidade nivel 3, ou seja, mórbida')