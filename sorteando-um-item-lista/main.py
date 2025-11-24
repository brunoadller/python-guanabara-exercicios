import random as rd
lista = []

for i in range(5):
    name = input(f"Informe o {i + 1}º aluno: ")
    lista.append(name)

print(f"\nO nome escolhido é: {rd.choice(lista)}")