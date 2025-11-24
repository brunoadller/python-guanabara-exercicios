from math import hypot
# h = sqrt(co^2 + ca^2)
co = float(input("Informe o comprimento do cateto oposto? "))
ca = float(input("Informe o comprimento do cateto adjacente? "))
h = (co**2 + ca**2)**(1/2)
print(f"A hipotenusa irá medir: {h:.2f}")
print(f"Utilizando a biblioteca math a hypotenusa é: {hypot(co, ca):.2f}")
