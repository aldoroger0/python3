##Calcular el descuento y el monto a pagar por un medicamento cualquiera
##en una farmacia si todos los medicamentos tienen un descuento del 35%
print("vienvenido al programa".center(50, "-"))
print("todos los productos tienen 35% de descuento")
MONTO = 0
DESCUENTO = 0.35

monto = int(input("ingrese valor de producto: "))
medicina = (monto * 0.35)
descuento = (monto - medicina)
print("su total de pago es: ",descuento)

    
 
