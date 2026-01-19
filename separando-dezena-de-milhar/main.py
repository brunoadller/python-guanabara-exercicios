numero = str(input("Informe um número: "))
print(f"Analisadno o numero {numero}")
letras = list(numero)#converte a string para uma lista

if len(numero) == 1:
    print(f'Unidade: {numero[-1]}')
    print(f'Dezena: 0')
    print(f'Centena:0')
    print(f'Milhar: 0')
elif len(numero) == 2:
    print(f'Unidade: {numero[-1]}')
    print(f'Dezena: {numero[-2]}')
    print(f'Centena:0')
    print(f'Milhar: 0')
elif len(numero) == 3:
    print(f'Unidade: {numero[-1]}')
    print(f'Dezena: {numero[-2]}')
    print(f'Centena: {numero[-3]}')
    print(f'Milhar: 0')
elif len(numero) == 4:
    print(f'Unidade: {numero[-1]}')
    print(f'Dezena: {numero[-2]}')
    print(f'Centena: {numero[-3]}')
    print(f'Milhar: {numero[-4]}')
elif len(numero) == 0 or int(numero) < 0 or int(numero) >= 10000:
    print("Por favor informe um número maior que zero!")