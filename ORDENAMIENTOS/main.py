'''
Ejercicio 4: Una startup desea analizar las estadísticas de los usuarios de su sitio de 
compras on-line recientemente lanzado al mercado para ello necesita un programa 
que le permita acceder a los datos relevados.
Agregar los siguientes puntos al Menú de Opciones:

9  - Listar los datos de los usuarios de México ordenados por nombre
10 - Listar los datos del/los usuario/s más joven/es ordenados por edad de manera ascendente (Si la edad se repite, ordenar por nombre de manera 
ascendente)
11 - Listar los datos de los usuarios de México y Brasil cuyo código postal 
sea mayor a 8000 ordenado por nombre y edad de manera descendente

Ejercicio 8: Crear una función para cada opción de menú.
Ejercicio 9: Desarrollar las funciones en una biblioteca.
'''

from lista_opciones import *
from listas_personas import *

continuar = "s"
import_inicializado = False


while continuar == "s":
        
        opcion_elegida = int(input("""[ MENU DE DATOS ]

Ingrese con un el numero asignado la opcion que se desea ejecutar:
                                
1)  Importar listas
2)  Listar los datos de los usuarios de México
3)  Listar los nombre, mail y teléfono de los usuarios de Brasil
4)  Listar los datos del/los usuario/s más joven/es
5)  Obtener un promedio de edad de los usuarios
6)  De los usuarios de Brasil, listar los datos del usuario de mayor edad
7)  Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000
8)  Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años
9)  Listar los datos de los usuarios de México ordenados por nombre
10) Listar los datos del/los usuario/s más joven/es ordenados por edad de manera ascendente (Si la edad se repite, ordenar por nombre de manera ascendente)
11) Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000 ordenado por nombre y edad de manera descendente
12) salir
                                   
--> Ingrese una opcion a elegir: """))
        opcion_elegida = verificar_opcion_elegida(opcion_elegida)

        print("#----------------------------------------------------------------------------------------#")

        if opcion_elegida == 1:

                nombres_c = nombres
                telefonos_c = telefonos
                mails_c = mails
                address_c = address
                postalZip_c = postalZip
                country_c = country
                region_c = region
                edades_c = edades

                import_inicializado = True
                print("[ DATOS IMPORTADOS ]\n")

                continuar = input("--> Desea continuar (s/n): ")
                continuar = verificar_menu(continuar)

        
        if opcion_elegida == 2:

                if import_inicializado == True:
                        user_data_mx(nombres_c, telefonos_c, mails_c, address_c, postalZip_c, country_c, region_c, edades_c)

                        continuar = input("--> Desea continuar (s/n): ")
                        continuar = verificar_menu(continuar)
                else:
                        print("[ ERROR ] No se ha importado primero las listas. \n")
        

        if opcion_elegida == 3:
                if import_inicializado == True:
                        user_contact_br(nombres_c, telefonos_c, mails_c, country_c)

                        continuar = input("--> Desea continuar (s/n): ")
                        continuar = verificar_menu(continuar)
                else:
                        print("[ ERROR ] No se ha importado primero las listas. \n")
        
        
        if opcion_elegida == 4:
                if import_inicializado == True:
                        younger_user_data(nombres_c, telefonos_c, mails_c, address_c, postalZip_c, country_c, region_c, edades_c)

                        continuar = input("--> Desea continuar (s/n): ")
                        continuar = verificar_menu(continuar)
                else:
                        print("[ ERROR ] No se ha importado primero las listas. \n")
        

        if opcion_elegida == 5:
                if import_inicializado == True:
                        avg_user_age(edades_c)

                        continuar = input("--> Desea continuar (s/n): ")
                        continuar = verificar_menu(continuar)
                else:
                        print("[ ERROR ] No se ha importado primero las listas. \n")
        

        if opcion_elegida == 6:
                if import_inicializado == True:
                        older_user_data_br(nombres_c, telefonos_c, mails_c, address_c, postalZip_c, country_c, region_c, edades_c)

                        continuar = input("--> Desea continuar (s/n): ")
                        continuar = verificar_menu(continuar)
                else:
                        print("[ ERROR ] No se ha importado primero las listas. \n")

        
        if opcion_elegida == 7:
                if import_inicializado == True:
                        user_data_postalZip_mx_br(nombres_c, telefonos_c, mails_c, address_c, postalZip_c, country_c, region_c, edades_c)

                        continuar = input("--> Desea continuar (s/n): ")
                        continuar = verificar_menu(continuar)
                else:
                        print("[ ERROR ] No se ha importado primero las listas. \n")


        if opcion_elegida == 8:
                if import_inicializado == True:     
                        user_data_it(nombres_c, telefonos_c, mails_c, edades_c, country_c)

                        continuar = input("--> Desea continuar (s/n): ")
                        continuar = verificar_menu(continuar)
                else:
                        print("[ ERROR ] No se ha importado primero las listas. \n")
        

        if opcion_elegida == 9:
                if import_inicializado == True:     
                        listar_por_nombre_asc_mx(nombres_c, country_c)

                        continuar = input("--> Desea continuar (s/n): ")
                        continuar = verificar_menu(continuar)
                else:
                        print("[ ERROR ] No se ha importado primero las listas. \n")
        

        if opcion_elegida == 10:
                if import_inicializado == True:     
                        younger_user_asc(nombres_c, telefonos_c, mails_c, address_c, postalZip_c, country_c, region_c, edades_c)

                        continuar = input("--> Desea continuar (s/n): ")
                        continuar = verificar_menu(continuar)
                else:
                        print("[ ERROR ] No se ha importado primero las listas. \n")
        

        if opcion_elegida == 11:
                if import_inicializado == True:     
                        user_data_mx_br_dsc(nombres_c, telefonos_c, mails_c, address_c, postalZip_c, country_c, region_c, edades_c)

                        continuar = input("--> Desea continuar (s/n): ")
                        continuar = verificar_menu(continuar)
                else:
                        print("[ ERROR ] No se ha importado primero las listas. \n")
        

        if opcion_elegida == 12:
                continuar = "n"


print("[ FIN DEL PROGRAMA ]")
