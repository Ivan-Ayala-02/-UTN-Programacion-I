# Crear una función lambda que indique si el número recibido es par o impar.

numero = int(input("Ingrese un numero: "))
evaluar_numero_par = lambda numero : f"{numero} es par." if numero % 2 == 0 else f"{numero} es impar."

print(evaluar_numero_par(numero))