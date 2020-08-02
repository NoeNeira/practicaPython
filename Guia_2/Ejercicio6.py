"""
Escribir un programa que seleccione una operación de 
cuatro operaciones numéricas disponibles, una vez seleccionada la operación, introducir dos números y ejecutar la operación.
"""

operacionNumerica = int(input("""Ingrese una operación númerica: 
1- Suma
2- Resta
3- Multiplición
4- División
"""))

n = int(input("Ingrese un nro."))
m = int(input("Ingrese otro nro."))

if operacionNumerica <= 4:
   if operacionNumerica == 1:
       print(n + m)
   elif operacionNumerica == 2:
       print(n - m)
   elif operacionNumerica == 3:
       print(n * m)
   elif operacionNumerica == 4:           
       print(int(n / m)) 
else: 
    print("nro. de operacion incorrecta; suma, resta, multiplicación o división")    
