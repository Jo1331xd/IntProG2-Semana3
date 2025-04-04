print("Salario neto de un empleado")
salario=int(input("Ingrese su salario "))

calculo1= salario * 0.10 
calculo2= salario * 0.05
calculo3= salario * 0.03

suma1= calculo1 + calculo2 + calculo3
salarioneto= salario - suma1

print(" el salario bruto es: ", salario)
print(" los descuento totales son: ", suma1)
print(" el salario neto es: ", salarioneto)
