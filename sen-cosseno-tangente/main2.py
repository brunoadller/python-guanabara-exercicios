import math as mt
angulo = int(input("Informe o ângulo que você deseja: "))
radianos = (angulo * mt.pi)/180
print(f'O seno de {angulo}° é: {mt.sin(mt.radians(angulo)):.2f}')
print(f'O cosseno de {angulo}° é: {mt.cos(mt.radians(angulo)):.2f}')
print(f'A tangente de {angulo}° é: {mt.tan(mt.radians(angulo)):.2f}')