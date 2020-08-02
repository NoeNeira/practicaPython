"""
Pedir al usuario que ingrese un mensaje cualquiera, si el mensaje tiene más de 100 caracteres 
imprimirlo por pantalla, si tiene entre 50 y 100 caracteres imprimirlo al revés, 
si no se cumple ninguna de las opciones anteriores, por pantalla devolver un mensaje que diga 
"su mensaje es demasiado corto"
"""

texto = input("Por favor ingrese un texto")

if len(texto) >= 100:
    print(texto)
elif 50 <= len(texto) and len(texto) < 100:
    print(texto[::-1])   
else:
    print("Su mensaje es demasiado corto")    

# str(a[::-1]))
# Return the slice of the string that starts at the end and steps backward one element at a time
# mensaje[start:stop:step]