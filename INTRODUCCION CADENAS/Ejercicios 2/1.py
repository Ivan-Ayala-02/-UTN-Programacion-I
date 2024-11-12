'''
1) Crear una función que reciba como parámetro una cadena y determine la
cantidad de vocales que hay de cada una (individualmente). La función
retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2
la cantidad.
Por ej:
cadena = “murcielaguito”
“a” 1
“e” 1
“i” 2
“o” 1
“u” 2
'''

def vocales(cadena:str):

    letra_a = 0
    letra_e = 0
    letra_i = 0
    letra_o = 0
    letra_u = 0

    cadena_minuscula = cadena.lower()

    for letra in cadena_minuscula:

        if letra == "a":
            letra_a += 1
        
        elif letra == "e": 
            letra_e += 1

        elif letra == "i":
            letra_i += 1

        elif letra == "o":
            letra_o += 1
        
        elif letra == "u":
            letra_u += 1

    vocales_total = [["a", letra_a],["e", letra_e],["i", letra_i],["o", letra_o],["u", letra_u]]

    return vocales_total

print(vocales("Texto de prueba"))