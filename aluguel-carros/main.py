km_percorrido = float(input("Informe a quantidade de Kilômetros percorridos? "))
qntd_dias = int(input("Informe a quantidade de dias que o carro foi alugado? "))
preço_pagar = (qntd_dias * 60) + (0.15 * km_percorrido)
print(f"O preço a pagar é: R$ {preço_pagar}")
