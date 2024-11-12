'''
Clase simple

Crear una clase Persona que tenga las características nombre y edad.  La persona debe poder 
mostrar un mensaje saludando presentándose con su nombre y edad.  Se debe crear la clase e 
implementarla
'''

class Persona:
    def __init__(self, nombre:str, edad:int) -> None:
        self.nombre = nombre
        self.edad = edad

    def imprimir_informacion(self) -> None:
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}")

persona_1 = Persona("Ivan", 22)
persona_1.imprimir_informacion()
