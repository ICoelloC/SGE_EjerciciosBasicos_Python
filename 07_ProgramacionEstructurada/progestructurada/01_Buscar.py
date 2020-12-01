#! /usr/bin/env python

def insertar_dni():
    dni_insertado = input("·DNI: ").upper()
    return dni_insertado


def insertar_alumno():
    alumno_insertado = ""
    is_palabra = False
    while not is_palabra:
        alumno_insertado = input("·NOMBRE: ").upper()
        is_palabra = True
    return alumno_insertado


def insertar_curso():
    curso_insertado = ""
    is_curso = False
    while not is_curso:
        curso_insertado = input("·CURSO: ").upper()
        is_curso = True
    return curso_insertado


def insertar_nota():
    nota_insertada = 0.0
    isNumerico = False

    while not isNumerico:
        try:
            nota_insertada = float(input("·NOTA: "))
            isNumerico = True
        except ValueError:
            print("Debes introducir un valor númerico correcto")
    return nota_insertada


def crear_diccionario(dni_param, alumno_param, curso_param, nota_param, diccionario_param):
    datos = [alumno_param, curso_param, nota_param]
    diccionario_param.setdefault(dni_param, datos)
    if dni_param not in diccionario_param:
        diccionario_param[dni_param].append(alumno_param)
        diccionario_param[dni_param].append(curso_param)
        diccionario_param[dni_param].append(nota_param)
    return diccionario_param


def buscar(listado_alumnos, **kwargs):
    for valor in kwargs.values():
        if valor in listado_alumnos.keys():
            dni_buscar = valor.upper()
            print("DATOS DE", dni_buscar)
            print(f"\t NOMBRE Y APELLIDOS: {listado_alumnos.get(dni_buscar)[0]}")
            print(f"\t CURSO: {listado_alumnos.get(dni_buscar)[1]}")
            print(f"\t NOTA: {listado_alumnos.get(dni_buscar)[2]}")
            print()
        elif valor.upper() in listado_alumnos.values():
            print("SIN HACER TODAVÍA")
        else:
            print("NO EXISTE")


if __name__ == "__main__":

    diccionarioClaves = {}
    condicion = ""

    while condicion != '*':
        dni = insertar_dni()
        alumno = insertar_alumno()
        curso = insertar_curso()
        nota = insertar_nota()
        diccionario_alumnos = crear_diccionario(dni, alumno, curso, nota, diccionarioClaves)
        print()
        condicion = input("ESCRIBA '*' SI DESEA SALIR, 'S' SI DESEA BUSCAR: ")
        print()
        if condicion == 'S':
            print()
            buscar(diccionarioClaves, valor="123")
