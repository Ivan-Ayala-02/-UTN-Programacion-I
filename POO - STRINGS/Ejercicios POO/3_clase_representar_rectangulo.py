'''
Clase para representar un Rectángulo 
Crear una clase rectángulo que tenga las características base y altura.  Del rectángulo se debe 
poder calcular el área y el perímetro.  Se debe crear la clase e implementarla.
'''

class Rectangulo:
    def __init__(self, base, altura) -> None:
        self.base = base
        self.altura = altura
    
    def area(self) -> float:
        area = self.base * self.altura
        print(f"Area: {area}")
    
    def perimetro(self) -> float:
        perimetro = (self.base * 2) + (self.altura * 2)
        print(f"Perimetro: {perimetro}")

    