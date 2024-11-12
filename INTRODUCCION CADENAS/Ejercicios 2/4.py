'''
4) Crear una función que reciba como parámetro una cadena y suprima los
caracteres repetidos.
Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.
'''

def suprimir_caracteres_repetidos(cadena:str):

    cadena_vacia = ""

    for letra in cadena:
        if letra not in cadena_vacia:
            cadena_vacia += letra

    return cadena_vacia

print(suprimir_caracteres_repetidos("hooool"))