"""
Crear una lista con varios números, luego ordenarlos de manera creciente y devolver 
por pantalla la lista ordenada y cuál es el menor y cuál el mayor.
"""

listaDeNumeros = [1, 5, 9, 10, 803, 342, 7, 78]

listaDeNumeros.sort()

print(listaDeNumeros)

mayor = max(listaDeNumeros)

print(mayor)

menor = min(listaDeNumeros)

print(menor)