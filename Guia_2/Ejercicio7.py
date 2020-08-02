"""
Crear un diccionario con 5 estudiantes y sus respectivas notas.
Imprimir por pantalla los alumnos que aprobaron y su nota (no en forma de diccionario, sino con nombre : nota).
Tener en cuenta que para aprobar el alumno debe sacarse una nota mayor o igual a 7 y menor o igual a 10.
"""

notasAlumnos = {
    "García": 10,
    "Suarez": 7,
    "Rodríguez": 2,
    "Gómez": 5,
    "Gonzalez": 6
}

for apellido, nota in notasAlumnos.items():
    if nota >= 7:
        print(f"{apellido}:{nota}")