# 4) Realizar una función para calcular el número de Fibonacci de un número ingresado por consola

def calcular_fibonacci(num:int):

    a = 0
    b = 1

    for i in range(num+1):

        c = a + b
        print(f"{i}) {a} + {b} = ", c)
        a = b
        b = c
        

numero = int(input("Ingrese un numero: "))
calcular_fibonacci(numero)