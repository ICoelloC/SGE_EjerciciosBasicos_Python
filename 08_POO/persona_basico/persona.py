class Persona:
    # inicializamos nuestros atributos
    def inicializar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # imprimimos los datos
    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)

    # comprobamos si es mayor de edad o no
    def mayor_edad(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")
