"""
Utilizar el método range() para recorrer el iterable 
e imprimir solo los números impartes entre 1 y 40 inclusive.
"""

lista = []

for i in range(1,40):
    if i % 2 != 0:
     lista.append(i) #identación

print(lista)    