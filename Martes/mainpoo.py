from cosas import Alumno


def main():
    """
    al1 = Alumno()
    print(al1)
    al2 = Alumno()
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)
    # Se crea otro atributo de instancia al hacer la siguiente
    #al1.facultad = "Fes aragon MEX"
    # para si cambiar el valor es con los siguiente
    # Alumno.facultad = "Fes aragon EDO MEX"
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)
    print("------- Un vistazo a los objetos ------")
    print(vars(al1))
    print(vars(al2))
    print("----- Modificar atributos publicos -----")
    al1.edad = 999
    print(vars(al1))
"""
    al1 = Alumno("Diego", 19, "ICO")
    al2 = Alumno("Monse", 20, "Derecho")
    print(vars(al1))
    al1.__edad = 333
    print(al1.__edad)
    print(vars(al1))


if __name__ == '__main__':
    main()
