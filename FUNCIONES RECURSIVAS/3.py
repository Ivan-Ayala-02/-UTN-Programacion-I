# 3) Realizar una función recursiva que permita realizar la suma de los dígitos de un número:

def sumar_digitos(numero:int)->int:
    if numero == 0:
        return 0
    else:
        return numero % 10 + sumar_digitos(numero // 10)
        '''
        Al hacer numero modulo 10 lo que logramos es obtener el ultimo digito
        Luego volvemos a invocar la funcion sumar_digitos
        Se hace una division entera para excluir el decimal
        (Ej: 123 -> 12.3 -> 12)
        '''
        
    
    # 123 ---> 1 + 2 + 3 ---> 6

numero = 111
print("La suma de los digitos del numero", numero ,"es de", sumar_digitos(numero))
