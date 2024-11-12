# 2) Realizar una función recursiva que calcule la potencia de un número

def calcular_potencia(base:int, exponente:int)->int:

    if base == 1 or exponente == 0:
        return 1
    else:
        resultado = base ** exponente
        return resultado

print(calcular_potencia(2,0))