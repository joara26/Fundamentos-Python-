'''. Crie um programa para controlar listas, com as seguintes funções:
• Adicionar elemento no início;
• Adicionar elemento no fim;
• Remover elemento;
• Tamanho da lista;
• Imprimir elementos da lista;
• Esvaziar lista;'''
team1 = input('Digite a equipa 1: ')
team2 = input('Digite a equipa 2: ')
team3 = input('Digite a equipa 3: ')
team4 = input('Digite a equipa 4: ')

camp = [team1, team2, team3, team4]

camp.insert(0, 'Fulham')  # Adiciona Fulham no início
camp.insert(len(camp), 'Wolves')  # Adiciona Wolves no fim


camp.remove(team4)  # Remove a última equipa informada pelo usuário, se existir

tamanho = len(camp)
print(f'A lista tem {tamanho} equipas:', camp)

camp.clear()  # Limpar a lista
print('A lista foi limpa')

