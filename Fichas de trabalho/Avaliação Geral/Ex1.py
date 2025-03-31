'''Leia uma cadeia de caracteres no formato “DD/MM/AAAA” e copie o dia, mês e ano para
três variáveis inteiras.'''

def extract_date_parts(date_str):
    try:
        day, month, year = map(int, date_str.split("/"))
        return day, month, year
    except ValueError:
        print("Formato inválido. Use DD/MM/AAAA.")
        return None

# Exemplo de uso
date_input = input("Digite uma data no formato DD/MM/AAAA: ")
date_parts = extract_date_parts(date_input)

if date_parts:
    day, month, year = date_parts
    print(f"Dia: {day}, Mês: {month}, Ano: {year}")
