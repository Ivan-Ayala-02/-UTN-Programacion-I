'''
Encapsulamiento 
Crear una clase Cuenta Bancaria que tenga las características titular y saldo encapsulado.  De la 
cuenta bancaria se puede obtener el saldo, depositar o retirar (en cada caso imprimir que fue 
exitoso).  Se debe crear la clase e implementarla.
'''

class CuentaBancaria:

    def __init__(self, titular:str, saldo:int|float):
        self.__titular = titular
        self.__saldo = saldo
    
    def obtener_saldo(self):
        return self.__saldo
    
    def depositar_saldo(self, saldo_ingresado):
        self.__saldo += saldo_ingresado
        print("Deposito Exitoso!")
    
    def retirar_saldo(self, saldo_retirado):
        if self.__saldo < saldo_retirado:
            print("Fondos insuficientes.")
        else:
            self.__saldo -= saldo_retirado
            print("Retiro Exitoso!")

cuenta_1 = CuentaBancaria("Ivan", 1000)

print(cuenta_1.obtener_saldo())

cuenta_1.depositar_saldo(100)
print(cuenta_1.obtener_saldo())

cuenta_1.retirar_saldo(500)
print(cuenta_1.obtener_saldo())