'''
Ejercicio 5: Desarrollar una función que capitalice palabras en una cadena.
'''

def capitalizar_letras(letra:str)->str:
    letra = letra.capitalize()
    return letra


letras = input("Ingrese una letra: ")
print(capitalizar_letras(letras))