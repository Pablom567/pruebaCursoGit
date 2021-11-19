
from time import time
from random import randint


def crear_lista(cantidad,desde,hasta):
    lista = []
    for i in range(cantidad):
        lista.append(randint(desde,hasta))
    return lista

# VARIABLE GLOBAL (OJO!: NO NOS GUSTAN)
comparaciones = 0


def bubbleSort(lista):
    global comparaciones
    n = len(lista)

    for i in range(1, n):
        for j in range(n-i):
            comparaciones += 1

            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]



def insertionSort(lista):
    n = len(lista)
    global comparaciones

    for i in range(1, n):
        val = lista[i]
        j = i

        while j > 0 and lista[j-1] > val:
            lista[j] = lista[j-1]
            j -= 1
            comparaciones += 1

        lista[j] = val

def mergeSort(lista):
    if len(lista) <= 1:
        return lista

    medio = int(len(lista) / 2)
    izquierda = lista[:medio]
    derecha = lista[medio:]

    izquierda = mergeSort(izquierda)
    derecha = mergeSort(derecha)

    return merge(izquierda, derecha)


def merge(listaA, listaB):
    global comparaciones
    lista_nueva = []
    a = 0
    b = 0

    while a < len(listaA) and b < len(listaB):
        comparaciones += 1

        if listaA[a] < listaB[b]:
            lista_nueva.append(listaA[a])
            a += 1
        else:
            lista_nueva.append(listaB[b])
            b += 1

    while a < len(listaA):
        lista_nueva.append(listaA[a])
        a += 1

    while b < len(listaB):
        lista_nueva.append(listaB[b])
        b += 1

    return lista_nueva


def particion(lista, izq, der):
    global comparaciones
    pivote = lista[der]
    indice = izq

    for i in range(izq, der):
        comparaciones += 1

        if lista[i] <= pivote:
            lista[indice], lista[i] = lista[i], lista[indice]
            indice += 1

    lista[indice], lista[der] = lista[der], lista[indice]
    return indice


def quicksort(lista, izq, der):
    if izq < der:
        pivote_indice = particion(lista, izq, der)
        quicksort(lista, izq, pivote_indice-1)
        quicksort(lista, pivote_indice+1, der)


def selectionSort(lista):
    global comparaciones
    n = len(lista)

    for i in range(n - 1):
        menor = i
        comparaciones += 1

        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]


def shellSort(lista):
    global comparaciones
    n = len(lista)
    gap = int(n / 2)

    while gap > 0:
        for i in range(gap, n):
            val = lista[i]
            j = i
            comparaciones += 1

            while j >= gap and lista[j-gap] > val:
                lista[j] = lista[j-gap]
                j -= gap

            lista[j] = val

        gap = int(gap / 2)

def main():
    global comparaciones
    lista = crear_lista(1000,1,1000)
    comparaciones=0
    t0 = time()
    shellSort(lista)
    t1 = time()

    print("Lista ordenada shellSort:")
    
    print("Tiempo: {0:f} segundos".format(t1 - t0))
    print("Comparaciones:", comparaciones)


    lista = crear_lista(1000,1,1000)
    comparaciones = 0
    t0 = time()
    selectionSort(lista)
    t1 = time()

    print("Lista ordenada selectionSort:")
    
    print("Tiempo: {0:f} segundos".format(t1 - t0))
    print("Comparaciones:", comparaciones)


    lista = crear_lista(1000,1,1000)
    comparaciones = 0
    t0 = time()
    quicksort(lista, 0, len(lista)-1)
    t1 = time()

    print("Lista ordenada quicksort:")
    
    print("Tiempo: {0:f} segundos".format(t1 - t0))
    print("Comparaciones:", comparaciones)


    lista = crear_lista(1000,1,1000)
    comparaciones = 0
    t0 = time()
    lista = mergeSort(lista)
    t1 = time()

    print("Lista ordenada mergeSort:")
    
    print("Tiempo: {0:f} segundos".format(t1 - t0))
    print("Comparaciones:", comparaciones)

    lista = crear_lista(1000,1,1000)
    comparaciones = 0
    t0 = time()
    insertionSort(lista)
    t1 = time()

    print("Lista ordenada insertionSort:")
    
    print("Tiempo: {0:f} segundos".format(t1 - t0))
    print("Comparaciones:", comparaciones)

    lista = crear_lista(1000,1,1000)
    comparaciones = 0
    t0 = time()
    bubbleSort(lista)
    t1 = time()

    print("Lista ordenada bubbleSort:")

    print("Tiempo: {0:f} segundos".format(t1 - t0))
    print("Comparaciones:", comparaciones)
    
    lista = crear_lista(1000,1,1000)
    comparaciones = 0
    t0 = time()
    lista.sort()
    t1 = time()

    print("Lista ordenada python:")

    print("Tiempo: {0:f} segundos".format(t1 - t0))
    print("Comparaciones:", comparaciones)

if __name__ == "__main__":
    main()
