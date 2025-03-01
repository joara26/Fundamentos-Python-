'''Considera a lista
idades=[25, 15, 19, 22, 37, 78, 46, 2, 67]
Cria um programa, em python, que:
a. Indique quantas pessoas são menores de idade
b. Ordene a lista por ordem decrescente
c. Pede ao utilizador uma idade e verifica se essa idade está na lista.
#- Se estiver faz print("A idade está na lista")
#- Caso contrário faz o print("não existe ninguém com essa idade na lista")
'''
idades=[25, 15, 19, 22, 37, 78, 46, 2, 67]
#Indique quantas pessoas são menores de idade
menores = [idade for idade in idades if idade < 18]
print(f"Quantidade de menores de idade: {len(menores)}")


#Ordene a lista por ordem decrescente
idades.sort(reverse=True)


#Pede ao utilizador uma idade e verifica se essa idade está na lista.
il = int(input('Digite uma idade para verificar se está presente na lista: '))
if il in idades:
    print(f'{il} está na lista')
else:
    print('Não existe ninguém com essa idade na lista')
    