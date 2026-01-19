valor_casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salário: "))
quantos_anos = int(input("Em quantos anos ira realizar o pagamento do empréstimo: "))
prestacao = valor_casa/(quantos_anos * 12)
valor_porcentagem_salario = (salario * 0.3)

if  prestacao > valor_porcentagem_salario:
    print("Emprestimo negado!")
else:
    print(f"Emprestimo concedido! Ficará {quantos_anos} parcelas de R${prestacao:.2f}")