t1 = float (input('resultado do teste 1:'))
t2 = float (input('resultado do teste 2:'))
t3 = float (input('resultado do teste 3:'))
m = (t1 + t2 + t3) % 3 
if m > 10 : print ('aprovado')
else: print ('reprovado')  # type: ignore