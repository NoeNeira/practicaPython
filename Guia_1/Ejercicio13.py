"""
Crear un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""

miDicc = {
    'Euro':'€', 
    'Dollar':'$', 
    'Yen':'¥'
    }

divisaEligida = input("Qué divisa desea elegir? Euro, Dollar o Yen? ")

if divisaEligida in miDicc:
    print(miDicc[divisaEligida]) 
else:
    print("No existe esa divisa en el diccionario")