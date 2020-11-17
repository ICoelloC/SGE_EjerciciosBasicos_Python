#! /usr/bin/env python
if __name__ == '__main__':
    fichero = open('utilidades/personas.txt', 'r', encoding="utf8")
    lineas = fichero.readlines()
    fichero.close()

    registros = []
    for registro in lineas:
        campos = registro.replace("\n", "").split(";")
        persona = {"id": campos[0], "nombre": campos[1], "apellido": campos[2], "nacimiento": campos[3]}
        registros.append(persona)

    for p in registros:
        print("id:", p['id'])
        print(" Nombre y apellidos:", p['nombre'], p['apellido'])
        print(" Fecha de nacimiento:", p['nacimiento'])
        print()
