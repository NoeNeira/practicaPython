"""
Pedir al usuario que ingrese un mensaje cualquiera, si el mensaje tiene más de 100 caracteres 
imprimirlo por pantalla, si tiene entre 50 y 100 caracteres imprimirlo al revés, 
si no se cumple ninguna de las opciones anteriores, por pantalla devolver un mensaje que diga 
"su mensaje es demasiado corto"
"""

texto = input("Por favor ingrese un texto")

if len(texto) > 100:
    print(texto)
elif len(texto) <= 50:
    print(texto.__reversed__)    