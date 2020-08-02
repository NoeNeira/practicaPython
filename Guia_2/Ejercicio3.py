"""
Pedir al usuario que ingrese por teclado 2 números, si el primero es menor que el segundo imprimir 
la resta entre el segundo y el primero, si el primero es mayor que el segundo imprimir la suma de ambos, 
y si son iguales imprimir su producto.
"""

n = int(input("Ingrese un nro"))
m = int(input("Ingrese otro nro"))

if n < m:
    print(m - n)
elif n > m:
    print(n + m)
elif n == m:
    print(n * m)
