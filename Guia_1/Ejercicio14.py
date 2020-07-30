"""
Crear un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
Después debe mostrar por pantalla el mensaje.
"""

nombre = input("Ingrese su nombre : ")
edad = (input("Ingrese su edad : "))
direccion = input("Ingrese su dirección : ")
telefono = (input("Ingrese su teléfono : "))

miDicc = {}
miDicc.__setitem__("nombre", nombre)
miDicc.__setitem__("edad", edad)
miDicc.__setitem__("dirección", direccion)
miDicc.__setitem__("teléfono", telefono)

print(miDicc)



