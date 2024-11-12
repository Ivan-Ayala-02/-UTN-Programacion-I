# Crear una función lambda que realice un 10% de descuento en el importe recibido.

importe = int(input("Ingrese el importe recibido: "))
descuento = 10

descuento_sobre_importe = lambda importe, descuento : importe - ((descuento * importe) / 100)

print(descuento_sobre_importe(importe, descuento))
