'''
Ejercicio 1: Dadas las siguientes listas:

Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

Desarrollar una función que realice el ordenamiento de las listas por nombre de manera ascendente.
'''

Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

def ordenar_nombres_asc(lista:list):

    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

    for i in range(len(lista)):
        print(lista[i])

ordenar_nombres_asc(Nombres)


