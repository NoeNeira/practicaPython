"""
Crear una función que devuelva True si los parámetros ingresados son todos números, False si hay al 
menos uno de los parámetros ingresados que no es un número, y None si ninguno de los parámetros 
ingresados es un número. Imprimir resultado por pantalla.
"""

def revisarParametros(*args):
    numeros = []
    
    for i in args:
        if type(i) == int:
            numeros.append(i)

    if len(numeros) == 0:
        return None
    elif len(numeros) == len(args):
        return True
    else:
        return False    

print((revisarParametros("casa", "arbol")))        
print((revisarParametros(1, 0))) 
print((revisarParametros("casa", 1))) 
print((revisarParametros()))    
