def iniciar_menu()->str:

   print('''
MENU DE OPCIONES -------------------------------------------------------------------
          
1) Listar los alumnos por orden ascendente
2) Promedio de notas para cada estudiante
3) Listar legajo, nombre, apellido y edad de los estudiantes que cursan el programa 
   de "ingenieria informatica"
4) Obtener promedio de edad de los estudiantes
5) Informar el alumno con mayor promedio de notas
6) Listar nombre y apellido de los alumnos que forman el grupo "Club de informatica"
   con sus respectivos promedios
7) Listar legajo, nombre, apellido y programas que cursan los alumnos 
   más jóvenes.
8) Salir
    ''')

   opcion = input("Ingrese opcion a elegir (1-8): ")

   while opcion.isdigit() == False or int(opcion) < 1 or int(opcion) > 8:

      if opcion.isdigit() == False:
         opcion = input("Ingrese un caracter numerico para elegir la opcion (1-7): ")

      elif int(opcion) < 1 or int(opcion) > 8:
         opcion = input("Ingrese opcion a elegir dentro del rango valido (1-7): ")
   
   print()

   return opcion



def volver_menu()->str:

   volver = input("Desea volver al menu (s/n): ")
   volver = volver.lower()

   while volver != "s" and volver != "n":
      volver = input("ingrese una opcion valida (s/n): ")
   
   return volver



def swapear_listas(elemento1, elemento2):
   aux = elemento1
   elemento1 = elemento2
   elemento2 = aux


def listar_nombre_ascendente(dic_alumnos:list):

   print("--- Listar los alumnos por orden ascendente ---\n")

   for i in range(len(dic_alumnos)-1):
      for j in range(i+1, len(dic_alumnos)):
         if dic_alumnos[i]["nombre"] > dic_alumnos[j]["nombre"]:
            aux = dic_alumnos[i]
            dic_alumnos[i] = dic_alumnos[j]
            dic_alumnos[j] = aux
   
   for e_alumno in dic_alumnos:
      print(e_alumno["nombre"])
   print()



def calcular_promedios_notas(diccionario_alumnos)->float:
   
   acumulador_notas = 0
   contador_notas = 0

   for i in range(len(diccionario_alumnos["notas"])):
      acumulador_notas += diccionario_alumnos["notas"][i]
      contador_notas += 1
   
   promedio = acumulador_notas/contador_notas
   return promedio



def mostrar_promedio_alumno(diccionario_alumno, promedio):
   print(f"Alumno: {diccionario_alumno["nombre"]} {diccionario_alumno["apellido"]}")
   print(f"Promedio: {promedio}\n")



def calcular_estudiantes_notas(lista_alumnos:list, opcion:str):


   print("--- Promedio de notas para cada estudiante ---\n")

   for i in range(len(lista_alumnos)):

      promedio = calcular_promedios_notas(lista_alumnos[i])

      if opcion == "promedio":
         mostrar_promedio_alumno(lista_alumnos[i], promedio)

      elif opcion == "mayor":
         if i == 0 or promedio > promedio_mayor:
            promedio_mayor = promedio
            pos_mayor = i
   
   if opcion == "mayor":
      mostrar_promedio_alumno(lista_alumnos[pos_mayor], promedio_mayor)   



def info_est_ing_informatica(dic_alumnos:list):

   print("--- Informacion de estudiantes (Ingenieria Informatica) ---\n")

   for i in range(len(dic_alumnos)):
      if dic_alumnos[i]["programa"]["nombre"] == "Ingenieria en Informatica":
         print(f"Legajo: {dic_alumnos[i]["legajo"]}")
         print(f"Nombre: {dic_alumnos[i]["nombre"]}")
         print(f"Apellido: {dic_alumnos[i]["apellido"]}")
         print(f"Edad: {dic_alumnos[i]["edad"]}\n")



def promedio_estudiante_edad(dic_alumnos:list):

   print("--- Promedio de edad estudiantes ---\n")

   acumulador_edad = 0

   for i in range(len(dic_alumnos)):
      acumulador_edad += dic_alumnos[i]["edad"]
   
   print(f"Promedio edad: {acumulador_edad/len(dic_alumnos)}\n")



def info_club_informatica(dic_alumnos:list):

   print("--- Informacion de estudiantes (Club de Informatica) ---\n")
   
   for alumno in dic_alumnos:
      contador_notas = 0
      acumulador_notas = 0

      if "grupos" in alumno:
         for grupo in alumno["grupos"]:

            if grupo["nombre"] == "Club de Informatica":
               print(f"Alumno: {alumno["nombre"]} {alumno["apellido"]}")

               contador_notas = 0
               acumulador_notas = 0

               for calificacion in alumno["notas"]:
                  acumulador_notas += calificacion
                  contador_notas += 1
               
               promedio = acumulador_notas/contador_notas
               print(f"Promedio: {promedio}\n")

               
         
def info_est_mas_joven(dic_alumnos:list):

   print("--- Informacion de estudiante/s mas joven/es ---\n")

   for i in range(len(dic_alumnos)):
      if i == 0 or dic_alumnos[i]["edad"] < edad_mas_joven:
         edad_mas_joven = dic_alumnos[i]["edad"]
   
   print(f"Edad mas joven: {edad_mas_joven}")

   for alumno in dic_alumnos:

      if alumno["edad"] == edad_mas_joven:
         print(f"Legajo: {alumno["legajo"]}")
         print(f"Nombre: {alumno["nombre"]}")
         print(f"Apellido: {alumno["apellido"]}")

         print(f"Programa:")
         for nombre_nivel in alumno["programa"]:
            if i%2 == 0:
               tipo = "    Nombre"
            if i%2 == 1:
               tipo = "    Nivel"
            i+=1
            print(f"{tipo}: {alumno["programa"][nombre_nivel]}")
         print()

            
      

         

         