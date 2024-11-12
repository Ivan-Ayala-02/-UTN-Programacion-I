'''
Ejercicio 6: Analizar los datos del archivo listas_personas.py. Utilizando el archivo 
listas_personas.py. Importar los nombres a una lista. Realizar una función que 
muestre los mismos.
'''

from listas_personas import nombres


def mostrar_nombres(lista:list):

    for i in range(len(lista)):
        print(f"{i+1})", lista[i])

mostrar_nombres(nombres)



