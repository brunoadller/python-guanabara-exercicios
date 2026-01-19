
salario = float(input("Informe seu salário para verificarmos o quanto houve de aumento: "))

if salario > 1250.00:
    aumento = (salario * 0.10) + salario
    print(f"Para o salário de R${salario:.2f}, houve um aumento de {0.10 * 100}%, o salário atual será R${aumento:.2f}")
else:
    aumento = (salario * 0.15) + salario
    print(f"Para o salário de R${salario:.2f}, houve um aumento de {0.15 * 100}%, o salário atual será R${aumento:.2f}")
    