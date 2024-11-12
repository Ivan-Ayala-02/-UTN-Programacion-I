'''
5) Crear una función que reciba una cadena por parámetro y suprima las
vocales de la misma.
Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”
'''

def suprimir_vocales(cadena:str):

    cadena_minuscula = cadena.lower()
    cadena_vacia = ""
    vocales = ["a", "e", "i", "o", "u"]

    for letra in cadena_minuscula:
        if letra not in vocales:
            cadena_vacia += letra

    return cadena_vacia

print(suprimir_vocales("eggs"))


