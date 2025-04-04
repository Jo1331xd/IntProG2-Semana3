print("Calculo índice de masa corporal IMC" )
peso=float(input("Ingrese su peso en kilogramos "))
altura_metros=float(input("Ingrese altura en metros "))

altura1= (float (altura_metros * 2))

imc= (float(altura1 // peso))


multiplicacion1= imc * 100
division1= imc / 100 

print(f"Peso ingresado: {peso} kg")
print(f"Altura ingresada: {altura1} m")
print(f"Peso imc estandar: {imc} kg")
print(f"Altura imc calculado: {division1} m")  