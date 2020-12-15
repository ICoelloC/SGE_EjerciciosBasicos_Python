import uuid
import json
import time
from pj import personajes

data = {}
data['personajes_creados'] = []


class Personaje():

    def __init__(self, nombre, raza, clase, vida, mana):
        self.nombre = nombre
        self.raza = raza
        self.clase = clase
        self.vida = vida
        self.mana = mana

    def configurarPersonaje(self):
        print("""\n ¿Qué personaje deseas crear?\n
        1) Humanos
        2) Orcos""")
        raza = input("\n> ")
        if raza == '1':
            raza = "Humanos"
            print("""\n¿Qué clase de humano deseas crear?\n
            1) Guerrero
            2) Jinete
            3) Mago """)
            clase = input("\n>")
            if clase == '1':
                clase = 'Guerrero'
                self.crearPersonaje(raza, clase)
            elif clase == '2':
                clase = 'Jinete'
                self.crearPersonaje(raza, clase)
            elif clase == '3':
                clase = 'Mago'
                self.crearPersonaje(raza, clase)
        elif raza == '2':
            raza = "Orcos"
            print("""\n¿Qué clase de orco deseas crear?\n
            1) Guerrero
            2) Chamán
            3) Jinete """)
            clase = input("\n>")
            if clase == '1':
                clase = 'Guerrero'
                self.crearPersonaje(raza, clase)
            elif clase == '2':
                clase = 'Chamán'
                self.crearPersonaje(raza, clase)
            elif clase == '3':
                clase = 'Jinete'
                self.crearPersonaje(raza, clase)
        else:
            print("\nHas introducido un comando inválido")

    def crearPersonaje(self, raza, clase):
        vida = personajes['Raza'][raza]['Clase'][clase]['Stats']['Vida']
        mana = personajes['Raza'][raza]['Clase'][clase]['Stats']['Mana']
        nombre = input("\nIntroduce el nombre de tu personaje > ")
        nuevo_pj = Personaje(
            nombre=nombre, raza=raza, clase=clase, vida=vida, mana=mana)
        datos = {
            "id": str(uuid.uuid4()),
            "Nombre": nuevo_pj.nombre,
            "Raza": nuevo_pj.raza,
            "Clase": nuevo_pj.clase,
            "Vida": nuevo_pj.vida,
            "Mana": nuevo_pj.mana
        }
        self.guardarPersonaje(datos)
        print("\nEl personaje \"{}\" ha sido creado".format(datos["Nombre"]))

    def guardarPersonaje(self, datos):
        data['personajes_creados'].append(datos)
        pjs = data['personajes_creados']
        archivo = open('Personajes.json', 'w')
        json.dump(pjs, archivo, indent=4)

    def cargarPersonajes(self):
        try:
            archivo = open('Personajes.json')
            data['personajes_creados'] = json.load(archivo)
        except FileNotFoundError:
            print("\nCreando registro de personajes...")
            time.sleep(1)
            archivo = open('Personajes.json', 'a+')
        except json.decoder.JSONDecodeError:
            print("\nNo hay personajes creados, crea nuevos personajes a partir de ahora;D")
            pass

    def interfaz(self):
        i = 0
        while True:
            print("""\n=== Bienvenido al creador de personajes humanos y orcos ===\n
            ¿Qué deseas hacer?\n
            1) Crear un personaje
            2) Ver los personajes creados
            3) Salir del programa\n""")
            opcion = input("> ")
            if opcion == '1':
                self.configurarPersonaje()
            elif opcion == '2':
                if data['personajes_creados'] == []:
                    print("\nNo se encuentran personajes registrados")
                for personaje in data['personajes_creados']:
                    print("""\nID: {}
                    Nombre: {}
                    Raza: {}
                    Clase: {}
                    Vida: {}
                    Mana: {}\n """.format(personaje['id'], personaje['Nombre'], personaje['Raza'], personaje['Clase'],
                                          personaje['Vida'], personaje['Mana']))
            elif opcion == '3':
                print("\nGracias por usar el programa;)")
                time.sleep(2)
                quit()
            else:
                print("\nHas introducido un comando inválido")


class Iniciar(Personaje):
    def __init__(self):
        self.cargarPersonajes()
        self.interfaz()


Iniciar()
