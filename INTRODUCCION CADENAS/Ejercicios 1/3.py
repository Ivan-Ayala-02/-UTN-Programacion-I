'''
Ejercicio 3: Desarrollar una función “char_at” que recibe una cadena y un número. 
Se debe retornar el caracter en la posición indicada por el número si ésta es válida. 
'''

def char_at(cadena:str, num:int)-> str|None:

    for pos in range(len(cadena)):
        if pos == num:
            pos_lista = cadena[pos]
            return pos_lista


cadena_texto = input("Ingrese texto: ")
pos = int(input("Ingrese la posicion a buscar: "))

letra_en_la_lista = char_at(cadena_texto, pos)

if letra_en_la_lista == None:
    print(f"Numero fuera del rango (0,{len(cadena_texto)-1})")
else:
    print(letra_en_la_lista)