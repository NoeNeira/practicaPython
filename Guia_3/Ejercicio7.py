"""
Crear una función que verifique si una palabra es un palíndromo o no.
En caso de que lo sea devolver por pantalla "La palabra es un palíndromo", 
en caso contrario, devolver "La palabra no es un palíndromo".
"""

# def compruebaPalindromo(palabra):
#     palabraAlReves = palabra[::-1].lower()
#     if palabraAlReves == palabra.lower():
#         print("La palabra es un palíndromo")
#     else:
#         print("La palabra no es un palíndromo")    

# compruebaPalindromo("Abba")

def compruebaPalindromo(palabra):
    palabraAlReves = ""
    for i in range(len(palabra),0,-1):
        palabraAlReves = palabraAlReves + palabra[i-1]
    print(palabraAlReves)     
    if palabraAlReves.lower() == palabra.lower():
        print("La palabra es un palíndromo")
    else:
        print("La palabra no es un palíndromo")
            
compruebaPalindromo("Abba")



# semana = "semana"
# for i in range(len(semana)):
#     print(semana[i])    

# lista = ["semana", "dias", "año"]
# for i in range(len(lista)):
#     print(lista[i])    

# for i in lista:
#     print(i)

# for i in range(30+1,0,-1):
#     print(i)    