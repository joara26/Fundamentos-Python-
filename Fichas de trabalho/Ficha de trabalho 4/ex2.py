#Implemente um programa que, dada uma letra (S, C ou V), indique o estado civil de
#uma pessoa.
ec = str(input('Digite a inicial do Estado Civil (S, C ,V)'))
match ec:
    case "S":
        print('Solteiro')
    case "C":
        print('Casado')
    case "V":
        print('Viuvo')
    case _:
        print('O seu estado civil é inválido')