'''
Ejercicio 5: Dadas las siguientes listas:

Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Ped
ro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

Desarrollar una función que reciba por parámetro la lista de edades, busque a las 
personas de menor edad (puede ser más de una) y las retorne. El programa 
principal deberá mostrar nombre y edad de los menores.
'''

def buscar_menor_edad(nombres:list, edades:list):

    menor_edad = edades[0]

    for i in range(len(edades)):
        if edades[i] < menor_edad:
            menor_edad = edades[i]
    
    for i in range(len(edades)):
        if edades[i] == menor_edad:
            print(nombres[i])
        


nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

menores = buscar_menor_edad(nombres, edades)

