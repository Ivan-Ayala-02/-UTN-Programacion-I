# Crear una función lambda que incremente un 10% en el sueldo recibido.

sueldo = int(input("ingrese su sueldo: "))

print((lambda sueldo : sueldo * 1.11)(sueldo)) 