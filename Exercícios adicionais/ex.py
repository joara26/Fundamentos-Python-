#fábrica YS
#formeiros e as suas distribuições na linha de produção
import math
num_toda_da_nota = int(input( 'Digita o numero total da nota: '))
f60 = num_toda_da_nota / round(60) 
f45 = num_toda_da_nota / round(45)
f35 = num_toda_da_nota / round(35)
num42 = int(input('42: '))
num41 = int(input('41: '))
num40 = int(input('40: '))
num39 = int(input('39: '))
num38 = int(input('38: '))
num37 = int(input('37: '))
num36 = int(input('36: '))
f42 = int(round(num42 / round(f60),0))
f41 = int(round(num41 / round(f60),0))
f40 = int(round(num40 / round(f60),0))
f39 = int(round(num39 / round(f60),0))
f38 = int(round(num38 / round(f60),0))
f37 = int(round(num37 / round(f60),0))
f36 = int(round(num36 / round(f60),0))
f422 = int(round(num42 / round(f45),0)) 
f412 = int(round(num41 / round(f45),0))
f402 = int(round(num40 / round(f45),0))
f392 = int(round(num39 / round(f45),0))
f382 = int(round(num38 / round(f45),0))
f372 = int(round(num37 / round(f45),0))
f362 = int(round(num36 / round(f45),0))
f423 = int(round(num42 / round(f35),0))
f413 = int(round(num41 / round(f35),0))
f403 = int(round(num40 / round(f35),0))
f393 = int(round(num39 / round(f35),0))
f383 = int(round(num38 / round(f35),0))
f373 = int(round(num37 / round(f35),0))
f363 = int(round(num36 / round(f35),0))
print (f'Se andarem 60 pares de formas, \n o numero 42 deverá ter {f42} pares \n o nuemro 41 deverá ter {f41} pares \n o numero 40 deverá ter {f40} pares \n o numero 39 deverá ter {f39} pares \n o numero 38 deverá ter {f38} pares \n o numero 37 deverá ter {f37} pares \n o numero 36 deverá ter {f36} pares \ne deverá dar {f60} voltas')
print (f'Se andarem 45 pares de formas, \n o numero 42 deverá ter {f422} pares \n o nuemro 41 deverá ter {f412} pares \n o numero 40 deverá ter {f402} pares \n o numero 39 deverá ter {f392} pares \n o numero 38 deverá ter {f382} pares \n o numero 37 deverá ter {f372} pares \n o numero 36 deverá ter {f362} pares \ne deverá dar {f45} voltas')
print (f'Se andarem 35 pares de formas, \n o numero 42 deverá ter {f423} pares \n o nuemro 41 deverá ter {f413} pares \n o numero 40 deverá ter {f403} pares \n o numero 39 deverá ter {f393} pares \n o numero 38 deverá ter {f383} pares \n o numero 37 deverá ter {f373} pares \n o numero 36 deverá ter {f363} pares \ne deverá dar {f35} voltas')