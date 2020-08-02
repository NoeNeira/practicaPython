"""
Crear una lista con 10 números enteros cualquiera. Indicar cuál es el número mayor y cuál es el número menor. 
Si al menos hay 3 números mayores a 100, imprimir esos números, si no, 
imprimir los números menores a 50 que formen parte de la lista.
"""

lista = [1, 2, 3, 92, 134, 45, 56, 32, 544, 10]
listaMenoresACien = []
listaMayoresACien = []

print(max(lista))
print(min(lista))

for num in lista:       
    if num >= 100:
        listaMayoresACien.append(num)
    if num < 100:
        listaMenoresACien.append(num)  

if len(listaMayoresACien) >= 3:
    print(listaMayoresACien)
else:
    print(listaMenoresACien)
