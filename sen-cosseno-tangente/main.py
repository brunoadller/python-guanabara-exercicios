import math as mt
def plural(angulo):
    return "s" if angulo > 1 else ""
angulo = float(input("Informe um ângulo: "))
print(f"O SENO de {angulo} grau{plural(angulo)} é: {mt.sin(mt.radians(angulo)):.2f}")
print(f"O COSSENO de {angulo} grau{plural(angulo)} é: {mt.cos(mt.radians(angulo)):.2f}")
print(f"A TANGENTE  de {angulo} grau{plural(angulo)} é: {mt.tan(mt.radians(angulo)):.2f}")

