'''Considere a seguinte variável que armazena uma string com um conjunto de
datas separadas pelo caracter “,”.
datas="12ago2021,02set2020,20jan2022,11out2019,09mar2020,10dez2022"
Escreve um programa em Python que
a. Armazene as diferentes datas numa string;
b. Imprima as datas correspondentes ao ano de 2022;
c. Crie uma noca lista (dias) e na mesma armazena o dia de cada uma das
datas. Ordene a lista de forma crescente e imprima a mesma.
'''
datas = "12ago2021,02set2020,20jan2022,11out2019,09mar2020,10dez2022"

#a
s_datas = datas.split(",")
print(s_datas)

#b
for x in s_datas:
    if "2022" in x:
        print(x)
        
#c
dias=[]
for x in s_datas:
    dias.append(int(x[:2]))
dias.sort()
print(dias)