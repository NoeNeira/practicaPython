"""
Crear una función que, a partir de un mensaje, 
nos devuelva una lista con todos los números, si los hay, que aparecen en dicho mensaje.
"""

def mostrarListaNums():
    listaNums = []
    mensaje = input("Escriba un mensaje")

    for i in mensaje:
        if i.isdigit():
            listaNums.append(i)
    print(listaNums)

mostrarListaNums()
