'''
3) Crear una función que reciba como parámetro una cadena y determine si la
misma es o no un palíndromo. Deberá retornar un valor booleano indicando
lo sucedido.
'''

def verificador_palindromo(cadena:str):

    cadena_minuscula = cadena.lower()

    for letra in range(len(cadena_minuscula)):
        if cadena_minuscula[letra] == cadena_minuscula[-letra-1]:
            verificacion = True
        else:
            verificacion = False
    
    return verificacion

print(verificador_palindromo("Anana"))
print(verificador_palindromo("Hola"))