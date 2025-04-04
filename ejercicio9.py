print("Cálculo del tiempo total de una película con comerciales ")
minutos=float(input("Ingrese cuanto dura la pelicula en minutos "))
duracion_comerciales=float(input("Ingrese la duracion de comerciales previos "))
pausas_comerciales=int(input("Ingrese la cantidad de cada pausa comercial "))

duracion_total= duracion_comerciales * pausas_comerciales

suma1= minutos + duracion_total

print(f"La duracion de la pelicula original es: {minutos: .2f}")

print(f"La duracion de los comerciales es: {duracion_total: .2f}")

print(f"La duracion de la proyeccion total es: {suma1: .2f}")