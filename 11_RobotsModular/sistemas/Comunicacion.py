class Comunicacion:

    def __init__(self):
        self.mensajes = []

    @property
    def mensajes(self):
        return self.__mensajes

    @mensajes.setter
    def mensajes(self, value):
        self.__mensajes = value

    def recibir(self, emisor, msg):
        mensaje = f"{type(emisor).__name__} => Mensaje: {msg} "
        self.mensajes.append(mensaje)

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} => Mensajes: {1}"
        mensaje = ""
        for i in self.mensajes:
            mensaje += "\r\n" + i + "\r\n"
        return msg.format(clase, mensaje)
