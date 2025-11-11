largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = largura * altura
quantidade_necessaria = area / 2
print(f"Sua parede tem a dimensão de {largura}X{altura} a sua área é de {area}m².\nPara pintar essa parede, você precisará de {quantidade_necessaria:.4f}l de tinta.")