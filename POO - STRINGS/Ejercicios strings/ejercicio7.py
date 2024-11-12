'''
Ejercicio 7: Desarrollar una función “ordenar” que recibe un string y un número (1 o -1).  Se debe retornar 
el string ordenado de manera ascendente (si recibió 1 por parámetros) o descendente (si recibió -1) 
Nota: Determinar parámetros y retornos de manera que las funciones sean genéricas y reutilizables. 
'''

def ordenar(cadena:str, numero:int)->str:

    lista_cadena = []

    for letra in range(len(cadena)):
        lista_cadena.append(cadena[letra])

    #print(lista_cadena)

    for i in range(len(lista_cadena)-1):
        for j in range(i+1, len(lista_cadena)):

            if numero == 1 and lista_cadena[i] > lista_cadena[j]:
                auxiliar = lista_cadena[i]
                lista_cadena[i] = lista_cadena[j]
                lista_cadena[j] = auxiliar
                    
            elif numero == -1 and lista_cadena[i] < lista_cadena[j]:
                auxiliar = lista_cadena[i]
                lista_cadena[i] = lista_cadena[j]
                lista_cadena[j] = auxiliar
    
    #print(lista_cadena)
    
    nueva_cadena = "".join(lista_cadena)
    return nueva_cadena

#------------------------------------------------------------------------#

cad = input("Ingrese una cadena: ")
while cad.isalpha() == False:
    cad = input("Ingrese un texto valido: ")


num = input('''Opciones de ordenamiento

(1)  Ascendente
(-1) Descendente

Ingrese la opcion numerica a elegir: ''')
while num != "1" and num != "-1":
    num = input("Ingrese un numero valido (1 / -1): ")


nueva_cad = ordenar(cad, int(num))
print(nueva_cad)