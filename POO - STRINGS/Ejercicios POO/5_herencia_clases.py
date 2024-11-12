'''
Herencia de clases 
Crear una clase Animal que tenga la característica nombre.  La clase Perro que herede de Animal 
las características y realice el sonido “guau guau”.  La clase Gato que herede de Animal las 
características y realice el sonido “Miau”.  Del gato y el perro se debe poder mostrar el sonido que 
realizan. Se debe crear la clase e implementarla. 
'''

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def sonido(self):
        print("Guau Guau")

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def sonido(self):
        print("Miau Miau")

perro_1 = Perro("Tobi")
gato_1 = Gato("Luna")

perro_1.sonido()
gato_1.sonido()
    