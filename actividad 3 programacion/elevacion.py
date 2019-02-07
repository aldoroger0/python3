##solicitar al usuario que selecione una opcion
##1)solocitar 2 numeros y elevar el primer numero al segundo numero
##2)solicitar 3 numeros y elevar el premero al segundo y el resultado elevarlo al primero

print("1.elevar el primer numero al segundo  2.elevar el preimero al segundo y el resultado elevar al promero".center(30,"-"))
opcion = input(":.")
if opcion == "1":
    numero1 = (input("ingrese primer numero"))
    numero2 = (input("ingrese segundo numero"))
    elevacion = int(numero1) ** int(numero2)
    print("La elevacion es :. {}".format(elevacion))
elif opcion == "2":
    numero1 = input("ingrese primer numero")
    numero2 = input("ingrese segundo numero")
    numero3 = input("ingrese tercer  numero")
    elevacion = int(numero1) ** int(numero2) ** int(numero3)
    print("La elevacion es :. {}".format(elevacion))
else:
    print("opcion no valida")
    
