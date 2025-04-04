print("calcula el área y perímetro de un rectangulo")
base_rectangulo=float(input("ingrese la base "))
altura_rectangulo=float(input("ingrese la altura "))
perimetro=float
area=float

area=base_rectangulo * altura_rectangulo
print(f"El area del rectangulo es: {area: .2f}")
multiplicacion_base= base_rectangulo * 2
multiplicacion_altura= altura_rectangulo * 2

perimetro= multiplicacion_altura + multiplicacion_base

print(f"El perimetro del area es {perimetro: .2f}")