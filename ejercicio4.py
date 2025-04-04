print("Cálcule el tiempo total de un viaje con escalas en horas ")
primertramo=int(input("Ingresar la duración del primer tramo del vuelo: ",))
primeraescala=int(input("Ingresar la duración de la primera escala: ",))
segundotramo=int(input("Ingresar la duración del segundo tramo del vuelo: ",))
segundaescala=int(input("Ingresar la duración de la segunda escala: ", ))
tercertramo=int(input("Ingresar la duración del tercer tramo del vuelo: ",))

suma1= primertramo + primeraescala
suma2= suma1 + segundotramo
suma3= suma2 + segundaescala
suma4= suma3 + tercertramo

print("El tiempo total del viaje es: ", suma4)
