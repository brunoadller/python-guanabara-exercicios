velocidade = float(input("Qual é a velocidade atual do carro? "))
vm = 80.0
multa = (velocidade - vm) * 7
if velocidade <= vm:
    print("Tenha um bom dia! Dirija com segurança!")
else:
    print(f"MULTADO! Você excedeu o limite permitido que é de {vm}Km/h")
    print(f"Você deve pagar uma multa de R${multa:.2f}!")
    print("Tenha um bom dia! Dirija com segurança!")
