# Ejercicio 7-8-9 ---------------------------------------------------------------------------------------------------------------

from lista_opciones import *
from listas_personas import *

continuar = "s"
import_inicializado = False


while continuar == "s":
        
        opcion_elegida = int(input("""[ MENU DE DATOS ]

Ingrese con un el numero asignado la opcion que se desea ejecutar:
                                
1) Importar listas
2) Listar los datos de los usuarios de México
3) Listar los nombre, mail y teléfono de los usuarios de Brasil
4) Listar los datos del/los usuario/s más joven/es
5) Obtener un promedio de edad de los usuarios
6) De los usuarios de Brasil, listar los datos del usuario de mayor edad
7) Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000
8) Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años
9) Salir
                                   
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
                continuar = "n"

print("[ FIN DEL PROGRAMA ]")