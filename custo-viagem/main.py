distancia = float(input("Qual é a distância da sua viagem? "))
print(f"Você está prestes a começar uma viagem de {distancia:.2f}Km.")
if distancia <= 200:
    total = distancia * 0.50
    print(f"O preço da sua passagem será de R${total:.2f}")
else:
    total = distancia * 0.45
    print(f"O preço da sua passagem será de R${total:.2f}")
    