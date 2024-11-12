'''
2) Crear una función que reciba una cadena y un caracter. La función deberá
devolver el índice en el que se encuentre la primera incidencia de dicho
caracter, o -1 en caso de que no esté
'''

def buscar_caracter_en_cadena(cadena:str, caracter:str):

    for letra in range(len(cadena)):
        if cadena[letra] == caracter:
            ubicacion_letra = letra
            return ubicacion_letra
    
    ubicacion_letra = -1
    return ubicacion_letra

print(buscar_caracter_en_cadena("ejemplo", "o"))
        