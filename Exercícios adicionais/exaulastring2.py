# Solicita ao utilizador que insira um texto
texto = input("Introduza um texto: ")

# Lista de pontuações a serem removidas
pontuacao = [".", ",", ":", ";", "!", "?"]

# Remove os sinais de pontuação
for p in pontuacao:
    texto = texto.replace(p, " ")

# Divide o texto em palavras e conta quantas existem
numPalavras = len(texto.split())

# Imprime o número de palavras
print("Número de palavras:", numPalavras)
