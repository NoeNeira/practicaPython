"""Escribir un programa que almacene todas las letras del abecedario y luego elimine las vocales y 
nos devuelva una lista sin las vocales, sin modificar la original
"""

abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r",
              "s", "t", "u", "v", "w", "x", "y", "z"]

vocales = ["a", "e", "e", "o", "u"]

nuevoAbecedario = []

# for letra in abecedario:
#     print(letra)


for letra in abecedario:
    if letra not in vocales:
        nuevoAbecedario.append(letra)

print(nuevoAbecedario)



