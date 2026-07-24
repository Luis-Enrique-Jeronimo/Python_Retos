"""/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */"""

cadena = input("Ingresa una cadena de texto: ")

def invertirTexto(cadena):

    resultado = ''

    for letra in cadena:
        resultado = letra + resultado
    return resultado

print(invertirTexto(cadena))