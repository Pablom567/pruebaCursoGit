#LEER UN ENTERO CON CONTROL DE ERROR DE TIPO DE DATO
def leer_int(cartel="Ing un entero:",desde=-999999999,hasta=999999999):
    salir = False
    numero = 0
    while not salir:
        try:
            numero = int(input(cartel))
            if numero < desde or numero > hasta:
                print("ERROR ==> Dato fuera de rango {} .. {} ".format(desde,hasta))    
            else:
                salir = True
        except:
            print("ERROR ==> Ingrese un numero entero")
    return numero

#LEER UN FLOAT CON CONTROL DE ERROR DE TIPO DE DATO
def leer_float(cartel):
    salir = False
    numero = 0.0
    while not salir:
        try:
            numero = float(input(cartel))
            salir = True
        except:
            pass #SIN MOSTRAR CARTEL DE ERROR
            #print("\nERROR ==> Ingrese un numero decimal\n")
    return numero
