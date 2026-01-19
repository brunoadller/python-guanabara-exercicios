import random


lista = []

for i in range(5):
    name = str(input(f'Nome do {i + 1}º aluno: '))
    lista.append(name)
    
    
    
print(f"O aluno sorteado foi: {random.choice(lista)}")