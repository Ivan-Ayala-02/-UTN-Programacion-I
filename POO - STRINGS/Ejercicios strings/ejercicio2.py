'''
Ejercicio 2: Desarrollar una función que cuente cuántas palabras hay en una cadena.
'''

def cantidad_palabras_str(cadena:str):
    cadena = cadena.split(' ')
    print(len(cadena))

cantidad_palabras_str("Texto de ejemplo")

    