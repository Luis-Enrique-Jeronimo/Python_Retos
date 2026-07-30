"""/*
 * Crea un programa se encargue de transformar un número
 * entero a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */"""



def convertidor_binario():

    dividendo = int(input("Ingresa cualquier número entero: "))

    cociente = dividendo / 2
    residuo = dividendo % 2
    

    while cociente > 0:

        dividento = cociente

        cociente = dividendo / 2
        residuo = dividendo % 2

        print(cociente)
        
        print(residuo)


convertidor_binario()