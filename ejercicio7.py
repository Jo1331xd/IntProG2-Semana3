print("Cálculo del precio final de un producto con impuestos y descuentos ")

precio=float(input("Precio original del producto "))
descuento=float(input("Ingrese el descuento ")) 

multiplicacion1= precio * descuento
division1= multiplicacion1 / 100 

precio_con_descuento= precio - division1

IVA=float(input("Ingrese el IVA"))

division2= IVA / 100

precio_final= precio_con_descuento + division2

print(f"el precio original es: {precio: .2f}")
print(f"el descuento aplicado es: {division1: .2f}")
print(f"el precio con descuento es: {precio_con_descuento: .2f}")
print(f"el IVA calculado es: {division2: .2f}")
print(f"el precio total es: {precio_final: .2f}")





