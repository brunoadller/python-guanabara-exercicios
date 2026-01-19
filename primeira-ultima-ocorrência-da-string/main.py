frase = str(input("Digite uma frase: ")).strip().lower()
new_frase = list(frase)
#cont = 0
#for i in range(len(new_frase)):
#    if 'a' == new_frase[i]:
#        cont += 1

print(f"Aletra A aparecer {frase.count('a')} vezes na frase.")
print(f'A primeira letra A apareceu na posição {frase.find('a') + 1}')
print(f'A ultima posição em que se encontra a letra A apareceu na posição {frase.rfind('a') + 1}')
