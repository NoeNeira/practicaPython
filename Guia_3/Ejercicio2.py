"""
Crear una función que devuelva una 
lista con todos los números pares del 0 al 100 inclusive. Imprimir esa lista por pantalla.
"""

def mostrarLista():
    lista = []
    for i in range(100):
        if i % 2 == 0:
            lista.append(i) #identación
    return lista        

print(mostrarLista())