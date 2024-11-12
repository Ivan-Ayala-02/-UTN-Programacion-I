# Crear una función lambda devuelva el doble del número recibido.

numero = int(input("Ingrese un numero: "))
doble_del_numero = lambda numero : numero * 2

print(f"El doble de {numero} es:", doble_del_numero(numero))