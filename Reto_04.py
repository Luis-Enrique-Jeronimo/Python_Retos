"""/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */"""

num1 = int(input("INGRESA UN NÚMERO: "))

def primos(num1):
    for n in range(2,num1):
        if num1 % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True



primos(num1)