"""
Crear una función que devuelva por pantalla un mensaje ingresado por parámetro pero en modo Title. 
Si el mensaje ya está en modo title, que devuelva por pantalla "El mensaje ya está en modo title: {mensaje}"
"""

def msjModoTitle(msj):
    if msj.istitle():
        print(f"El mensaje ya está en modo title: {msj}")
    else:
        msjnuevo = msj.title()
        print(msjnuevo)

msjModoTitle("Hola, Soy Noelia ")
