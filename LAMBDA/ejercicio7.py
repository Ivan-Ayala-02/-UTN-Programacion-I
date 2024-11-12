# Crear una función lambda que devuelva el texto “femenino” si recibe el valor “f” y sino “masculino”.

genero = input("Ingrese genero (f/m): ")
evaluar_genero = lambda genero : "Femenino" if genero == "f" else "Masculino"

print(evaluar_genero(genero))