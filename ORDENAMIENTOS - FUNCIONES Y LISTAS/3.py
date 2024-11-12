'''
Ejercicio 3: Desarrollar una función que pida 10 números dentro de un rango 
especificado, validar los números solicitados dentro de ese rango, guardar en una 
lista y retornarla. El programa principal debe invocar a la función y mostrar por 
pantalla el retorno.
'''

def ingreso_numeros():
    lista = [0] * 10

    for i in range (len(lista)):
        num = int(input(f"{i+1}) Ingrese un numero dentro de el rango admitido (0-100): "))
        while num < 0 or num > 100:
            num = int(input("[ERROR] Ingrese un numero en un rango valido (0-100): "))
        lista[i] = num
    
    return lista

lista_numeros = ingreso_numeros()
print("Los numeros ingresados fueron:", lista_numeros)