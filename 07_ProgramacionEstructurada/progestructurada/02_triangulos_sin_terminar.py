def anadirTriangulo():
    nombre_triangulo = "Triangulo ", contador_triangulos
    coordenada_x = int(input("Indica la primera coordenada"))
    coordenada_y = int(input("Indica la segunda coordenada"))
    area = calcularArea(coordenada_x, coordenada_y)
    longitud = calcular_longitud()

    diccionarioTriangulos[nombre_triangulo] = coordenada_x, coordenada_y, area, longitud
    print(diccionarioTriangulos)


def calcularArea(x, y):
    area = (x * y) / 2
    return area


def calcular_longitud():
    longitud = 1

    return longitud


if __name__ == '__main__':
    contador_triangulos = 1
    diccionarioTriangulos = {}
    mensaje = "s"
    while mensaje == "s":
        anadirTriangulo()
        contador_triangulos = contador_triangulos + 1
        mensaje = input("¿Quieres añadir mas triangulos?")
