
values = []

while len(values) < 3:
    value = input(f"Informe o {len(values) + 1}º valor: ")
    try:
        value = int(value)
        values.append(value)
    except ValueError:
        print("Informe um número inteiro válido")
        
      
 
print(f"O maior valor informado foi: {max(values)}")
print(f"O menor valor informado foi: {min(values)}")
