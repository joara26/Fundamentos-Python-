'''Elabora uma script em python que peça ao utilizador um número e some todos
os números de 1 até esse mesmo número. Deves utilizar o tratamento de
erros.
'''
def somar_numeros():
    try:
        # Solicita ao usuário um número
        numero = int(input("Digite um número inteiro: "))
        
        if numero < 1:
            print("Digite um número maior ou igual a 1.")
            return
        
        # Calcula a soma dos números de 1 até o número informado pelo utilizador
        soma = sum(range(1, numero + 1))
        print(f"A soma de todos os números de 1 até {numero} é: {soma}")
    
    except ValueError:
        print("Erro: Você não digitou um número inteiro válido.")
    
# Chama a função para executar
somar_numeros()
