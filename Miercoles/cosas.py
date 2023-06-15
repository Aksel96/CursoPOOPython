class Alumno:
    facultad = "FES Aragón"

    def __init__(self, nom, ed, carr):
        self.__nombre = nom
        self.__edad = ed
        self.__carrera = carr

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_edad(self, edad):
        if 8 <= edad < 120:
            self.__edad = edad
        else:
            print("Esa edad no es correcta")
            self.__edad = 0

    def get_edad(self):
        return self.__edad

    def set_carrera(self, carrera):
        self.__carrera = carrera

    def get_carrera(self):
        return self.__carrera

    def __str__(self):
        cadena = "+--------------------------+\n"
        cadena = cadena + " Nombre: " + self.__nombre
        cadena = cadena + "\n Edad: " + str(self.__edad)
        cadena = cadena + "\n Carrera: " + self.__carrera
        cadena = cadena + "\n+--------------------------+"
        return cadena

    def estudiar(self, horas=1):
        print(f"El alumno {self.__nombre} esta estudiando por {horas} horas")


class Perro:
    reino = "Canino"

    def __init__(self, raza, edad, estatura):
        self.__raza = raza
        self.__edad = edad
        self.__estatura = estatura

    # Metodo de acceso GET
    @property
    def raza(self):
        return self.__raza

    # Metodo de acceso SET
    @raza.setter
    def raza(self, la_raza):
        self.__raza = la_raza

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        if 0 < edad <= 20:
            self.__edad = edad
        else:
            print("Esa no es una edad valida")
            self.__edad = 0

    @property
    def estatura(self):
        return self.__estatura

    @estatura.setter
    def estatura(self, estatura):
        if 0.10 < estatura <= 1.1:
            self.__estatura = estatura
        else:
            print("No Way")
            self.__estatura = 0.1

    def __str__(self):
        return f"""
            +-----------------------------+
            | Raza: {self.__raza}           |
            | Edad: {self.__edad}                     |
            | Estatura: {self.__estatura}              |
            +-----------------------------+"""

    @staticmethod
    def es_cachorro(edad):
        return edad < 3

    @staticmethod
    def dormir(veces=5):
        for i in range(veces):
            print(f"Dando vuelta {i + 1}")
        print("zZzzZZzZzzZz")

    @classmethod
    def perro_grande(cls, estatura):
        if estatura > 0.79:
            return cls("", 0, estatura)
