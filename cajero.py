


def main():
    importe = 54216# ==> 54220
    
    caja_1000 = 1000
    caja_500 = 1000
    caja_200 = 1000
    caja_100 = 1000
    caja_50 = 1000
    caja_20 = 1000
    caja_10 = 1000

    cant_1000 = 0
    cant_500 = 0
    cant_200 = 0
    cant_100 = 0
    cant_50 = 0
    cant_20 = 0
    cant_10 = 0

    importe_aux = importe
    while importe_aux >= 1000 and caja_1000 > 0:
        caja_1000 -= 1
        cant_1000 += 1
    
    print("Hola")
    print("Qué tal")
    

if __name__ == "__main__":
    main()
