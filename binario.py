
def esBinario(strbinario):
    if (strbinario.isdigit()):
        if all(caracter in '01' for caracter in strbinario):
            return True
    return False

try:
    print("")
    num_bin = input("Introduce un número binario: ")
    if (esBinario(num_bin)):
        print("El valor decimal de " + str(num_bin) + " es " + str(int(num_bin, 2)))
    else:
        print("El valor introducido no es un número binario")
except:
    print("Se ha producido un error inesperado. Por favor, inténtelo de nuevo")
