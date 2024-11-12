'''
Ejercicio 1: Desarrollar una función que Invierte el orden de los caracteres en una 
cadena.
'''

def invertir_cadena(cadena:str)->str:
    
    invertida = []
    cadena_invertida = ""

    print(cadena)

    for i in range(len(cadena)-1, -1, -1):
        invertida.append(cadena[i])

    cadena_invertida = cadena_invertida.join(invertida)
    print(cadena_invertida)

cadena = input("Ingrese texto: ")
invertir_cadena(cadena)

    
        