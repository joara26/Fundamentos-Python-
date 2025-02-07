'''Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.'''
    
    
s = float(input('Digite o salário: '))   
if s <= 280 :
    ns = s * 0.20 
    sf = ns + s 
    print (f'o aumento deve ser de 20%, ou seja deve ser aumentado cerca de {ns}, portanto deverá receber cerca de {sf}')
elif s <= 700 :
    ns2 = s * 0.15
    sf2 = ns2 + s 
    print (f'o aumento é de  15%, ou seja deve ser aumentado cerca de {ns2}, portanto deverá receber cerca de: {sf2}')
elif s <= 1500 :
    ns3 = s * 0.10
    sf3 = ns3 + s
    print (f'o aumento é de 10%, ou seja deverá ser aumentado cerca de {ns3}, portanto deverá receber cerda de: {sf3}')
else :
    ns4 = s * 0.05
    sf4 = ns4 + s
    print (f'o aumento é de 5%, ou seja deverá ser aumentado cerca de {ns4}, portanto deverá receber cerca de: {sf4}')
