"""
Crear una función que, a partir de un dato de entrada que sea en horas, nos informe cuántos minutos 
y cuántos segundos serían esas horas. Imprimir por pantalla dichos valores.
"""

def mostrarMinSeg(horas):
    minutos = horas * 60
    segundos = minutos * 60
    print(f"{horas} hora/horas representan {minutos} minutos")
    print(f"{horas} hora/horas representan {segundos} segundos")

print(mostrarMinSeg(5))
