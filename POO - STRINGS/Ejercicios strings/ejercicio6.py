'''
Ejercicio 6: Desarrollar una función que verifique si una cadena es un palíndromo: 
Palíndromo: Palabra o frase cuyas letras están dispuestas de tal manera que resulta 
la misma leída de izquierda a derecha que de derecha a izquierda; por ejemplo, 
anilina.
'''

def palindromo(cadena:str)->bool:

    cadena = cadena.lower()

    for letra in range(len(cadena)):

        if cadena[letra] == cadena[-letra-1]:
            verificacion = True
        else:
            verificacion = False
            return verificacion
 
    return verificacion

#---------------------------------------------#

cadena = input("Ingrese un texto: ")

while cadena.isalpha() == False:
    cadena = input("Ingrese un texto valido: ")

if palindromo(cadena):
    print("Es palindromo")
else:
    print("No es palindromo")