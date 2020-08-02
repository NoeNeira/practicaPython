"""
Ejercicio 4: Ingresar 6 números por teclado,
preferentemente enteros, 
ordenarlos de manera creciente e imprimirlos por pantalla.
"""

listaNumeros = []

for num in range(6):
    num = int(input("Ingrese un nro.: "))
    listaNumeros.append(num)
    listaNumeros.sort()
    
for num in listaNumeros:
    print(num)