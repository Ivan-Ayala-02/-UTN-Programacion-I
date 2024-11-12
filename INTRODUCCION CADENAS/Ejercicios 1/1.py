'''
Ejercicio 1: Desarrollar una función que reciba una letra y una cadena.
Debe retornar las veces que la letra está incluida en el texto.
'''

def letras_cadenas(letra:str, cadena:str)->int:
    contador = 0

    for caracter in cadena:
        if caracter == letra:
            contador += 1
    
    return contador

texto = "Esto es un texto de prueba"
letra = "o"
letras_encontradas = letras_cadenas(letra, texto)

print(f"Las veces que fueron encontradas la letra \"{letra}\" dentro de la cadena fueron un total de: {letras_encontradas}.")