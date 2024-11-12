def user_data_mx(nombres_c:list, telefonos_c:list, mails_c:list, address_c:list, postalZip_c:list, country_c:list, region_c:list, edades_c:list):

    for i in range(len(country_c)):
        if country_c[i] == 'Mexico':
            print(
                f"Nombre: {nombres_c[i]}\n" 
                f"Telefono: {telefonos_c[i]}\n" 
                f"E-mail: {mails_c[i]}\n" 
                f"Direccion: {address_c[i]}\n" 
                f"Codigo Postal: {postalZip_c[i]}\n" 
                f"Pais: {country_c[i]}\n" 
                f"Ciudad: {region_c[i]}\n" 
                f"Edad: {edades_c[i]}\n"
                )
            
def user_contact_br(nombres_c:list, telefonos_c:list, mails_c:list, country_c):
    for i in range(len(country_c)):
        if country_c[i] == 'Brazil':
            print(
                f"Nombre:{nombres_c[i]}\n" 
                f"Telefono:{telefonos_c[i]}\n" 
                f"E-mail:{mails_c[i]}\n"
                )

def younger_user_data(nombres_c:list, telefonos_c:list, mails_c:list, address_c:list, postalZip_c:list, country_c:list, region_c:list, edades_c:list):

    usuario_mas_joven = edades_c[0]

    for i in range(len(edades_c)):
        if edades_c[i] < usuario_mas_joven:
            usuario_mas_joven = edades_c[i]
    
    for i in range(len(edades_c)):
        if edades_c[i] == usuario_mas_joven:
            print(
                f"Nombre: {nombres_c[i]}\n" 
                f"Telefono: {telefonos_c[i]}\n" 
                f"E-mail: {mails_c[i]}\n" 
                f"Direccion: {address_c[i]}\n" 
                f"Codigo Postal: {postalZip_c[i]}\n" 
                f"Pais: {country_c[i]}\n" 
                f"Ciudad: {region_c[i]}\n" 
                f"Edad: {edades_c[i]}\n"
                )

def avg_user_age(edades_c:list):
    contador_edades = 0

    for i in range(len(edades_c)):
        contador_edades += edades_c[i]
    
    promedio = contador_edades / len(edades_c)
    print(f"Promedio de edades: {promedio}")

def older_user_data_br(nombres_c:list, telefonos_c:list, mails_c:list, address_c:list, postalZip_c:list, country_c:list, region_c:list, edades_c:list):
    usuario_mas_viejo = edades_c[0]

    for i in range(len(country_c)):
        if country_c[i] == 'Brazil':
            if edades_c[i] > usuario_mas_viejo:
                usuario_mas_viejo = edades_c[i]

    for i in range(len(country_c)):
        if country_c[i] == 'Brazil':
            if edades_c[i] == usuario_mas_viejo:
                print(
                    f"Nombre: {nombres_c[i]}\n" 
                    f"Telefono: {telefonos_c[i]}\n" 
                    f"E-mail: {mails_c[i]}\n" 
                    f"Direccion: {address_c[i]}\n" 
                    f"Codigo Postal: {postalZip_c[i]}\n" 
                    f"Pais: {country_c[i]}\n" 
                    f"Ciudad: {region_c[i]}\n" 
                    f"Edad: {edades_c[i]}\n"
                    )

def user_data_postalZip_mx_br (nombres_c:list, telefonos_c:list, mails_c:list, address_c:list, postalZip_c:list, country_c:list, region_c:list, edades_c:list):

    for i in range(len(postalZip_c)):
        if postalZip_c[i] > 8000:
            if country_c[i] == 'Mexico' or country_c[i] == 'Brazil':
                print(
                    f"Nombre: {nombres_c[i]}\n" 
                    f"Telefono: {telefonos_c[i]}\n" 
                    f"E-mail: {mails_c[i]}\n" 
                    f"Direccion: {address_c[i]}\n" 
                    f"Codigo Postal: {postalZip_c[i]}\n" 
                    f"Pais: {country_c[i]}\n" 
                    f"Ciudad: {region_c[i]}\n" 
                    f"Edad: {edades_c[i]}\n"
                    )

def user_data_it(nombres_c:list, telefonos_c:list, mails_c:list, edades_c:list, country_c:list):

    for i in range(len(country_c)):
        if country_c[i] == 'Italy':
            if edades_c[i] > 40:
                print(
                    f"Nombre:{nombres_c[i]}\n" 
                    f"Telefono:{telefonos_c[i]}\n" 
                    f"E-mail:{mails_c[i]}\n"
                    )
                
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def verificar_menu(continuar:str)->str:
    while continuar != "s" and continuar != "n":
        continuar = input("[ ERROR ] Ingrese una opcion valida (s/n): ")
    
    print("#----------------------------------------------------------------------------------------#")
    return continuar

def verificar_opcion_elegida(opcion_elegida:int)->int:
    while opcion_elegida < 1 or opcion_elegida > 9:
        opcion_elegida = int(input("[ ERROR ] Ingrese una opcion dentro del rango valido (1-9): "))
    
    return opcion_elegida