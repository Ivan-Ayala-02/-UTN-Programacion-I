import Ejercicio_est.opciones_est as op
from Ejercicio_est.estudiantes import *

continuar = "s"

while continuar == "s":

    opcion = op.iniciar_menu()

    if opcion == "1":
        op.listar_nombre_ascendente(estudiantes)
        continuar = op.volver_menu()
    
    elif opcion == "2":
        op.calcular_estudiantes_notas(estudiantes, "promedio")
        continuar = op.volver_menu()
    
    elif opcion == "3":
        op.info_est_ing_informatica(estudiantes)
        continuar = op.volver_menu()
    
    elif opcion == "4":
        op.promedio_estudiante_edad(estudiantes)
        continuar = op.volver_menu()
    
    elif opcion == "5":
        op.calcular_estudiantes_notas(estudiantes, "mayor")
        continuar = op.volver_menu()
    
    elif opcion == "6":
        op.info_club_informatica(estudiantes)
        continuar = op.volver_menu()

    elif opcion == "7":
        op.info_est_mas_joven(estudiantes)
        continuar = op.volver_menu()
    
    elif opcion == "8":
        continuar = "n"

    else:
        print(f"Error opcion {opcion}")

print("\n--- FIN DEL PROGRAMA ---\n")

