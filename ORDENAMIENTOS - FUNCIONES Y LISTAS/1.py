'''
Ejercicio 1: Desarrollar una función que pida 10 nombres de manera secuencial, los 
guarde en una lista y la retorne. El programa principal debe invocar a la función y
mostrar por pantalla el retorno.
'''

def lista_nombres()->list:
    lista = []

    for i in range (10):
        nombre = input(f"{i+1}) Ingrese nombre: ")
        lista.append(nombre)
    
    return lista

# ------------------------------------------------------

print("Los nombres ingresados fueron", lista_nombres())