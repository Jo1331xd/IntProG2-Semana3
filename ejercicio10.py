print("Cálculo de volumen de un cilindro y su área superficial")

radio=float(input("Ingrese el radio: "))
altura=float(input("ingrese la altura: "))

area_base= (float(3.141592 * (radio * radio)))

volumen_cilindro= altura * area_base

area_lateral= 2 * 3.141592 * altura
area_total= area_lateral + area_base + area_base

print(f"La altura es de: {altura: 2f}")
print(f"el radio es de: {radio: 2f}")
print(f"el volumen calculado es de: {volumen_cilindro: 2f}")
print(f"La area superficial es de: {area_total: 2f}")