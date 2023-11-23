
def estaEnRango(valor, minimo, maximo):
    if (minimo <= valor <= maximo):
        return True
    return False

def estaEnLista(valor, lista):
    if (valor in lista):
        return True
    return False

num = int(input("Introduce un número comprendido entre 1 y 20: "))
lista = [6, 14, 11, 3, 2, 1, 15, 19]

if (estaEnRango(num, 1, 20)):
    if (estaEnLista(num, lista)):
        print("El número " + str(num) + " está en la lista")
    else:
        print("El número " + str(num) + " no está en la lista")
else:
    print("El número " + str(num) + " no está comprendido entre 1 y 20")