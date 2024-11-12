# Crear una función lambda que indique si el número recibido es positivo o negativo.

numero = int(input("Ingrese un numero: "))
verificar_numero_positivo = lambda numero : f"{numero} es positivo" if numero > 0 else f"{numero} es negativo"

print(verificar_numero_positivo(numero))
