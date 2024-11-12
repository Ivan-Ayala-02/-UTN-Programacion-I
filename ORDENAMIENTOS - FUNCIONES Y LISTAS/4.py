'''
Ejercicio 4: Desarrollar una función que reciba por parámetro, una lista de números 
y un número especificado. La misma debe buscar el número especificado en la lista 
y retornar “True” si existe
'''

def buscar_numero(lista:list, numero:int)->bool:

    for i in range (len(lista)):
        if lista[i] == numero:
            return True
    
    return False
        
lista_numeros = [0,5,2,9,6]
numero = int(input("Ingrese numero a buscar: "))

if buscar_numero(lista_numeros, numero):
    print(f"El numero {numero} esta dentro de la lista.")
else:
    print(f"El numero {numero} NO esta dentro de la lista.")