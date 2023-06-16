from cosas import *


def main():
    per1 = Persona("Jose",19)
    print(per1)
    print(Persona.descripcion)

    print("--- Herencia alumno ---")
    al1 = Alumno("Jose",19,"23455","ICO")
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Juan"
    al2.dormir()

    print("--- Herencia Profe ---")
    profe1 = Profesor("Jesus",30 + 16,363565,"Ingenieria de Software")
    print(profe1)
    profe1.dormir()

    print("--- Herencia Ayudante Profe ---")
    ayudante = AyudanteProfesor("Juan",12,1212,"ICO",12333,"Ingenieria de Software",12)
    print(ayudante)
    ayudante.dormir()
    ayudante.nombre = "Abraham"
    ayudante.dar_clase("P.O.O")


if __name__ == '__main__':
    main()