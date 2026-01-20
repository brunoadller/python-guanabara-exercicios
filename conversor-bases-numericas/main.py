import math as mt

    
while True:
    number = int(input('Informe um  número inteiro: '))
    print("Escolha as bases de conversão: ")
    print("[1] Converter para BINÁRIO.")
    print("[2] Converter para OCTAL.")
    print("[3] Converter para HEXADECIMAL.")
    print("[4] Encerrar Programa.")
    

    choice = int(input("Digite a opção escolhida:  "))
    if choice == 1:
        print(f"{number} convertido para binário é {bin(number)[2:]}")
    if choice == 2:
        print(f"{number} convertido para octal é {oct(number)[2:]}")
    if choice == 3:
        print(f"{number} convertido para hexadecimal {hex(number)[2:]}")
    if choice == 4:
        print("Obrigado, até a próxima!")
        break
