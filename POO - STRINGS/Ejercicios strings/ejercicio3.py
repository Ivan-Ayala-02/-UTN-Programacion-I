'''
Ejercicio 3: Desarrollar una función que reemplaza una palabra específica por otra 
en una cadena.
'''

def reemplazar_palabra(cadena:str, palabra_antigua:str, palabra_nueva:str):
    cadena_nueva = cadena.replace(palabra_antigua, palabra_nueva)
    return cadena_nueva

cadena = "Vamos a desayunar"
print(reemplazar_palabra(cadena, "desayunar", "cenar"))