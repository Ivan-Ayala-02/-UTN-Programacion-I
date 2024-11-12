'''
Dadas las siguientes nombress:

Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion",
"Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"]

Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]

Desarrollar una función que realice el ordenamiento de las nombress por nombre de 
manera ascendente, si el nombre es el mismo, debe ordenar por puntos de manera 
descendente.
'''

Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]

def ordenar_nombres_asc(nombres:list, puntos:list):

    for i in range(len(nombres)-1):

        for j in range(i+1,len(nombres)):

            if nombres[i] > nombres[j]:

                aux = nombres[i]
                aux2 = puntos[i]

                nombres[i] = nombres[j]
                nombres[j] = aux
                puntos[i] = puntos[j]
                puntos[j] = aux2
            
            if nombres[i] == nombres[j]:

                if puntos[i] < puntos[j]:

                    aux = nombres[i]
                    aux2 = puntos[i]

                    nombres[i] = nombres[j]
                    nombres[j] = aux
                    puntos[i] = puntos[j]
                    puntos[j] = aux2


    for i in range(len(nombres)):
        print("Nombre:", nombres[i])
        print("Puntaje:", puntos[i])
        print()


ordenar_nombres_asc(Nombres, Puntos)
