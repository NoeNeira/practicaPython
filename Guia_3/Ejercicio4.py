"""
Crear una función que, a partir de 4 números,devuelva el mayor producto de dos de ellos. 
Imprimir resultado por pantalla.
"""

def productoMayor():
    listaNumeros = []
    for i in range(4):
        n = int(input("Ingrese un número: "))
        listaNumeros.append(n)     
    listaNumeros.sort()

    for num in listaNumeros:
        if num == 0:
            listaNumeros.pop(num)
            producto = listaNumeros[-2] * listaNumeros[-1]
        else:
            producto = listaNumeros[-2] * listaNumeros[-1]
    print(producto)

 ##Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.

productoMayor()