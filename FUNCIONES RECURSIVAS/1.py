# 1) Realizar una función recursiva que calcule la suma de los primeros números naturales:

def sumar_naturales(numero:int)->int:
    if numero == 1:
        return 1
      
    else:
        return numero + sumar_naturales(numero - 1)


numero = 2
print("La suma de los primeros", numero, "numeros naturales es de:", sumar_naturales(numero))