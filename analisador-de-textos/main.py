

name = str(input("Informe seu nome completo: "))
print('Analisando seu nome... ')
print(f"Seu nome em maiúsculas é: {name.upper()}")
print(f"Seu nome em minúsculas é: {name.lower()}")
print(f"Seu nome tem ao todo: {len(name.replace(" ", ""))}")
print(f'Seu primeiro nome é: {name.split()[0]} e ele tem {len(name.split()[0])} letras')

