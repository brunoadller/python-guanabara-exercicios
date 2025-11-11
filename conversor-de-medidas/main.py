medida = float(input("Informe a medida em metros: "))
km = medida /1000
hm = medida /100
dam = medida /10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f"\nA medida de {medida}m corresponde a: ")

print(f"\nEm Kilômetros: {km}km")
print(f"\nEm Hectômetros: {hm}hm")
print(f"\nEm Decâmetros: {dam}dam")
print(f"\nEm Decímetros: {dm}dm")
print(f"\nEm Centímetros: {cm}cm")
print(f"\nEm Milímetros: {mm}mm")
