'''
Ejercicio 3: Dadas las siguientes listas:

Estudiantes =["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Anto
nio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui"
,"Mitre","Andrade","Loza","Antares","Roca","Perez"]
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]

Desarrollar una función que realice el ordenamiento de las listas por apellido de 
manera ascendente, si el apellido es el mismo, debe ordenar por nombre de manera 
ascendente, si el nombre también es el mismo, debe ordenar por nota de manera 
descendente.
'''

Estudiantes =["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui","Mitre","Andrade","Loza","Antares","Roca","Perez"]
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]

def ordenar_estudiantes_asc(estudiantes:list, apellidos:list, nota:list):

    for i in range(len(estudiantes)-1):

        for j in range(i+1,len(estudiantes)):

            if apellidos[i] > apellidos[j]:

                aux = estudiantes[i]
                aux2 = apellidos[i]
                aux3 = nota[i]

                estudiantes[i] = estudiantes[j]
                estudiantes[j] = aux
                apellidos[i] = apellidos[j]
                apellidos[j] = aux2
                nota[i] = nota[j]
                nota[j] = aux3

            if apellidos[i] == apellidos[j]:

                if estudiantes[i] > estudiantes[j]:

                    aux = estudiantes[i]
                    aux2 = apellidos[i]
                    aux3 = nota[i]

                    estudiantes[i] = estudiantes[j]
                    estudiantes[j] = aux
                    apellidos[i] = apellidos[j]
                    apellidos[j] = aux2
                    nota[i] = nota[j]
                    nota[j] = aux3

                if estudiantes[i] == estudiantes[j]:

                    if nota[i] < nota[j]:

                        aux = estudiantes[i]
                        aux2 = apellidos[i]
                        aux3 = nota[i]

                        estudiantes[i] = estudiantes[j]
                        estudiantes[j] = aux
                        apellidos[i] = apellidos[j]
                        apellidos[j] = aux2
                        nota[i] = nota[j]
                        nota[j] = aux3

    for i in range(len(Estudiantes)):
        print("Apellido:", apellidos[i])
        print("Nombre:", estudiantes[i])
        print("Puntaje:", nota[i])
        print()


ordenar_estudiantes_asc(Estudiantes, Apellidos, Nota)
