'''
Ejercicio 2: Desarrollar una función que reciba una cadena y dos índices. 
Se debe retornar la cadena que va entre las posiciones indicadas por los índices. 
Si las posiciones no son válidas se debe informar.
'''

def indices_cadena(indice_1:int, indice_2:int, cadena:str)-> str|None:

    if indice_1 < 0 or indice_2 > len(cadena) or indice_1 > indice_2:
        return None

    nueva_cadena = cadena[indice_1:indice_2]
    return nueva_cadena
    

texto = input("Ingrese un texto: ")
num_1 = int(input("Ingrese un numero de inicio: "))
num_2 = int(input("Ingrese un numero a terminar: "))

texto_acortado = indices_cadena(num_1, num_2, texto)

if texto_acortado == None:
    print(f"Posicion no valida, ingresar dentro del rango 0-{len(texto)}")
else:
    print(texto_acortado)
