'''
Clase para representar un Libro 
Crear una clase Libro que tenga las características títuto, autor y año de publicación.  Del libro se 
debe poder obtener información, mostrando por mensaje todos sus datos.  Se debe crear la clase 
e implementarla. 
'''

class Libro:
    def __init__(self, title:str, author:str, year:int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def imprimir_informacion(self) -> None:
        print(f"Titulo: {self.title}\nAutor: {self.author}\nAño de publicacion: {self.year}")

libro_1 = Libro("1984", "George Orwell", 1949)
libro_1.imprimir_informacion()