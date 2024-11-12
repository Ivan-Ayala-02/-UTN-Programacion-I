'''
Ejercicio 2: Desarrollar una función que inicialice una lista de 10 números en 0, pida 
posición y número a guardar al usuario, lo guarde en una lista en la posición 
solicitada aleatoriamente y la retorne. El programa principal debe invocar a la 
función y mostrar por pantalla el retorno.
'''

def numero_posicion() -> list:
    lista = [0] * 10

    num = int(input("Ingrese un número: "))
    
    pos = int(input("Ingrese la posición del número en la lista (0-9): "))
    while pos < 0 or pos >= len(lista):
        pos = int(input("[ERROR] Ingrese la posición dentro de un rango válido (0-9): "))
    
    lista[pos] = num
    return lista

salida = numero_posicion()
print("Resultado:", salida)