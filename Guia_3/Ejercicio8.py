"""
Crear una función que calcule cuántos litros de nafta gasta un auto que consume 2 litros x 100km,
en un viaje ida y vuelta MdP-Bue si la distancia es de 400km.
Luego crear una función que, a partir de esos datos,
devuelva cuánto significa eso en pesos si el litro de nafta está 60$.
"""

def getConsumoEnLitros(km):
    return (km / 100) * 2

def getConsumoEnPesos(km):
    return getConsumoEnLitros(km) * 60

print(getConsumoEnLitros(400))
print(getConsumoEnPesos(400))