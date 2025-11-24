import random
lista = []

for i in range(4):
    name = input(f"Nome do {i + 1}º aluno: ")
    lista.append(name)

print("A ordem de apresentação será: ")
#da para utilizar sorted ou print(sorted(lista))
print(random.shuffle(lista))