print("-=-"*20)
print("Analisador de Triângulos: ")
print("-=-"*20)

segmentos = []
for i in range(3):
    segmento = float(input(f"{i+1}º segmento: "))
    segmentos.append(segmento)


if  ((segmentos[0] + segmentos[1]) > segmentos[2]) and (segmentos[0] + segmentos[2]) > segmentos[1] and (segmentos[1] + segmentos[2]) > segmentos[0]:
    print("Os segmentos acima PODEM FORMAR triângulo!")
else:
    print("Os segmentos acima NÃO PODEM FORMAR triângulo!")
    