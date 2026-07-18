"""/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */"""


def area_poligono(ladoA, ladoB):
    triangulo = ladoA * ladoB / 2
    poligono = ladoA * ladoB

    print(f"El área del Triangulo es: {triangulo}")
    print(f"El área del Cuadrado es: {poligono}")
    print(f"El área del Rectángulo es: {poligono}")

area_poligono(4,30)