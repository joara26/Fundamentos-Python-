'''Cria ou faz download de um ficheiro CSV. De seguida cria um programa
que leia o ficheiro CSV e mostre cada linha do mesmo.'''
import csv

# Caminho do ficheiro CSV
csv_filename = "funcionarios.csv"  #ficheiro está na mesma pasta do script

# Ler e exibir o ficheiro CSV
with open(csv_filename, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for linha in reader:
        print(linha)  # Exibe cada linha do ficheiro

