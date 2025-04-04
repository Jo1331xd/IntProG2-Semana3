print("Conversión de unidades de tiempo")
segundos=float(input("ingrese total de segundos "))
horas= segundos / 3600

multiplicacion1= horas * 3600
resta1= segundos - multiplicacion1
minutos= resta1 / 60 
multiplicacion2= minutos * 60

resta2= resta1 - multiplicacion2

print(f"Segundos: {multiplicacion2:.2f}")
print(f"minutos:  {minutos: .2f}")
print(f"Horas: {horas: .2f}")
