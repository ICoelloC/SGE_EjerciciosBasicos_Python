from utilities.Utils import Utils


class Motor:
    def __init__(self):
        self.id = Utils.generarint(1, 200)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    def __str__(self):
        return f"Id del motor: {id}"
