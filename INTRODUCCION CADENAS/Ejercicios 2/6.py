'''
6) Crear una función para contar cuántas veces aparece una subcadena dentro
de una cadena.
Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá
retornar el valor 2.


Mensaje: como no encontre una forma de hacer que no sea con cosas que aun no hemos visto,
intente pensarlo a mi manera, asi que va a haber descripciones para saber yo el por que y como
funciona esto.
'''

def cantidad_palabras_repetidas(cadena:str, subcadena:str):
    
    cadena_minuscula = cadena.lower()

    # PARTE 1

    # Primero buscamos separar la cadena por espacios, una vez conocida su ubicacion
    # determinamos las posiciones dentro de una lista (ya inicializada anteriormente desde la pos 0)
    # desde donde empiezan hasta donde terminan. Esto lo utilizaremos para mas tarde

    posicion_cadena_separada = [0]

    for caracter in range(len(cadena_minuscula)):
        
        if cadena_minuscula[caracter] == " ":
            posicion_cadena_separada.append(caracter)
            posicion_cadena_separada.append(caracter+1)

    posicion_cadena_separada.append(len(cadena_minuscula))

    # PARTE 2

    # Una vez que tengo las posiciones para cortar la cadena, inicio un ciclo que empieza por la
    # posicion inicial 0, la cantidad de elementos de la cadena de posiciones, y por ultimo, que haga una
    # iteracion saltando de a dos.
    # El objetivo de esto es que, con la iteracion llamada "posicion" salte cada vez al inicio del siguiente numero,
    # y que en la iteracion actual sume el lumero que le falta para completar el recorrido
    # Ej: i=0 [0 : 0+1]     i=2 [2 : 2+1]   i=4 [4 : 4+1]
    # En ejecucion dentro de este ejercicio, la iteracion posicion la utilizo para sacar la posicion de la listas
    # de cadenas separadas, y ya con la ubicacion que estaba dentro de las listas utilizo el rango de estas para
    # hacer el corte en la cadena principal y hacer la busqueda de la subcadena.

    palabras_repetidas = 0

    for posicion in range(0,len(posicion_cadena_separada),2):

        '''
        esto lo utilizo para validar que la separacion de cadenas sea correcta:
        
        print(cadena[posicion_cadena_separada[posicion] : posicion_cadena_separada[posicion+1]])
        '''

        if subcadena in cadena[posicion_cadena_separada[posicion] : posicion_cadena_separada[posicion+1]]:
            '''
            Toma la cadena y la corta por las posiciones anteriormente guardadas, y de ahi busca entre cada corte
            la subcadena, si la encuentra agrega un numero al contador, devolviendo este al final de la funcion el total
            de veces encontradas 
            '''
            palabras_repetidas +=1
    
    return palabras_repetidas




print(cantidad_palabras_repetidas("panadero con el pan de la panaderia", "pan"))


'''
Esto aun tiene errores como si la cadena es "panpanpan", solo lo tomara como 1 palabra repetida, pero estos son mis avances
hasta ahora.
'''


