'''. Considere a seguinte variável:
Txt="""Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos,
funcional, de tipagem dinâmica e forte."""
Escreve um programa em Python que
a. Imprima o texto anterior todo em maiúsculas;
b. Peça uma palavra ao utilizador e verifique se a mesma está ou não no
texto, devolvendo o resultado ao utilizador.
c. Imprima o número de vezes que a letra ‘O’ ocorre no texto
d. Substitua todaa as ocorrências da letra ‘P’ no texto por ‘_’
'''
Txt="""Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos,
funcional, de tipagem dinâmica e forte."""


#a
Txt=Txt.upper()
print(Txt)

#b
palavra= input('Digite a palvra que pretende pesquisar na frase').upper()
if palavra in Txt:
    print(f'A palavra {palavra} está na frase')
else:
    print(f'A palavra {palavra} não está na frase')
    
#c
print('No texto tem', Txt.count('O') ,"letras 'O'")

#d
print(Txt.replace("P", "_"))