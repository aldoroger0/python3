##Una tienda ofrese un descuento del 15% sobre el total de la compra y un cliente
##desea saber cuanto debera pagar finalmente por su compra

compra = int(input("ingrese cantidad de compra:."))
descuento = compra * 0.15
print("su descuento de la compra es:{}".format(compra))
print(" es de: {}".format(descuento))
print("su total a pagar es de:{}".format(compra - descuento))
