import random as R

# archivo = open("archivo.txt")
# for i, línea in enumerate(archivo):
#     línea = línea.rstrip("\\n")
#     print " %4d: %s" % (i, línea)
# archivo.close()


def creaArchivoOrdenado(cantidad, nombreArchivo="numeros.txt"):
    archivo = open(nombreArchivo, 'w')
    numero = 1
    while cantidad > 0:
        n = R.randint(1, 100)
        if n < 80:
            x = R.randint(0, 3)
            for i in range(x):
                archivo.write(str(numero)+'\n')
            archivo.write(str(numero)+'\n')
            cantidad -= 1
        numero += 1

    archivo.close()


def aparear():
    arch1 = open("numeros1.txt",'r')
    arch2 = open("numeros2.txt",'r')
    arch3 = open("apareado.txt",'w')
    #print(str(help))

    lin1 = arch1.readline()
    lin2 = arch2.readline()
    while lin1 != "" and lin2 != "":
        n1 = int(lin1)
        n2 = int(lin2)
        if n1 <= n2:
            arch3.write(str(n1) + " a1\n")
            lin1 = arch1.readline()
        else:
            arch3.write(str(n2) + " a2\n")
            lin2 = arch2.readline()
    while lin1 != "":
        n1 = int(lin1)
        arch3.write(str(n1) + " a1\n")
        lin1 = arch1.readline()
    while lin2 != "":
        n2 = int(lin2)
        arch3.write(str(n2) + " a2\n")
        lin2 = arch2.readline()
    arch1.close()
    arch2.close()
    arch3.close()


def main():
    creaArchivoOrdenado(1000, "numeros1.txt")
    creaArchivoOrdenado(1000, "numeros2.txt")
    aparear()


main()
