import random as rd

print("-=-"*20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-"*20)

sort = rd.randint(0, 5)
number = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
if number == sort:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print(f"Ganhei, eu pensei no número {sort} e não no {number}")
    