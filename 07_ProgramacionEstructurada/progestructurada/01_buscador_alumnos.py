#! /usr/bin/env python
def agregar_alumno(almacen, nomb, apell, identificador):
    alumno = {"nombre": nomb, "apellidos": apell}
    """Si el dni existía en el almacén será sobreescrito"""
    almacen[identificador] = alumno


def mostrar_alumnos(almacen):
    for identificador, alumno in almacen.items():
        print("DNI:", identificador, alumno)


def cumple_filtro_alumnos(alumno, kwargs):
    alumno_buscado = True
    for key, value, in kwargs.items():
        if key != "dni" and alumno_buscado and alumno[key] != value:
            alumno_buscado = False
    return alumno_buscado


def buscar_alumnos(almacen, **kwargs):
    """Optimizar búsqueda por dni"""
    resultados_busqueda = []
    if "dni" in kwargs.keys():
        try:
            alumno = almacen[kwargs["dni"]]
            alumno_buscado = cumple_filtro_alumnos(alumno, kwargs)
            if alumno_buscado:
                resultados_busqueda.append(alumno)
        except KeyError:
            pass
    else:
        almacen_filtrado = almacen.values()
        for alumno in almacen_filtrado:
            alumno_buscado = cumple_filtro_alumnos(alumno, kwargs)
            if alumno_buscado:
                resultados_busqueda.append(alumno)

    return resultados_busqueda


if __name__ == '__main__':
    almacen_alumnos = {}
    parar = False
    nombre = ""
    apellidos = ""
    dni = ""
    while not parar:
        print("Introduzca los datos del alumno (S para salir)")
        nombre = input("Nombre: ")
        if nombre != "S":
            apellidos = input("Apellidos: ")
            if apellidos != "S":
                dni = input("DNI: ")
            else:
                parar = True
        else:
            parar = True
        if not parar:
            agregar_alumno(almacen_alumnos, nombre, apellidos, dni)

    mostrar_alumnos(almacen_alumnos)
    print("BUSCANDO POR DNI", buscar_alumnos(almacen_alumnos, dni="456"))
    print("BUSCANDO POR DNI DE UN REGISTRO, Y NOMBRE DE OTRO",
          buscar_alumnos(almacen_alumnos, dni="123", nombre="Maria"))
    print("BUSCANDO SIN VALOR", buscar_alumnos(almacen_alumnos))
    print("BUSCANDO POR NOMBRE DE ALUMNO", buscar_alumnos(almacen_alumnos, nombre="Guillermo"))
