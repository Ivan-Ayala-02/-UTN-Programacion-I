# Crear una función lambda que informe si una persona es mayor (mayor a 17 años) o menor.

edad = int(input("Ingrese una edad: "))
evaluar_edad = lambda edad : "Es mayor de edad" if edad > 17 else "Es menor de edad"

print(evaluar_edad(edad))